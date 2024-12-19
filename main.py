from fastapi import FastAPI, Depends, HTTPException
from typing import Optional, List
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import get_db, ItemModel, init_db

app = FastAPI(title="TestAPI", 
             description="A simple REST API built with FastAPI",
             version="1.0.0")

# Pydantic model for request/response
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    is_available: bool = True

    class Config:
        from_attributes = True

# Initialize database tables on startup
@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/")
async def root():
    return {"message": "Welcome to TestAPI!", "status": "online"}

@app.post("/items/", response_model=Item)
async def create_item(item: Item, db: AsyncSession = Depends(get_db)):
    db_item = ItemModel(**item.dict())
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ItemModel).filter(ItemModel.id == item_id))
    db_item = result.scalar_one_or_none()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.get("/items/", response_model=List[Item])
async def list_items(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ItemModel).offset(skip).limit(limit))
    items = result.scalars().all()
    return items
