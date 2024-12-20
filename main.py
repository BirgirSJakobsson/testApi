from fastapi import FastAPI, Depends, HTTPException
from typing import Optional, List
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import get_db, ItemModel, init_db
import os
from dotenv import load_dotenv

# Determine which environment to load
# $env:APP_ENV="development"
# $env:APP_ENV="testing"
# $env:APP_ENV="production"
environment = os.getenv("APP_ENV", "development")  # Default to development
dotenv_file = f".env.{environment}"
load_dotenv(dotenv_file)  # Load the corresponding .env file

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

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
    print(f"Starting application in {os.getenv('APP_ENV', 'development')} environment")
    await init_db()

@app.get("/")
async def root():
    response_data = {
        "message": "Welcome to TestAPI!",
        "status": "online",
        "endpoints": [
            {"path": "/", "method": "GET", "description": "Welcome message, status of the API, and a list of all available endpoints"},
            {"path": "/items/", "method": "POST", "description": "Create a new item"},
            {"path": "/items/{item_id}", "method": "GET", "description": "Retrieve an item by ID"},
            {"path": "/items/", "method": "GET", "description": "List items with pagination"},
            {"path": "/docs", "method": "GET", "description": "API documentation"},
            {"path": "/docs/json", "method": "GET", "description": "API documentation in JSON format"},
            {"path": "/items/{item_id}", "method": "DELETE", "description": "Delete an item by ID"}
        ]
    } 
    return response_data

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

@app.get("/docs")
async def get_docs():
    return {
        "endpoints": [
            {"path": "/", "method": "GET", "description": "Welcome message and status"},
            {"path": "/items/", "method": "POST", "description": "Create a new item"},
            {"path": "/items/{item_id}", "method": "GET", "description": "Retrieve an item by ID"},
            {"path": "/docs", "method": "GET", "description": "API documentation"}
        ]
    }

@app.get("/docs/json")
async def get_docs_json():
    return {
        "endpoints": [
            {"path": "/", "method": "GET", "description": "Welcome message and status"},
            {"path": "/items/", "method": "POST", "description": "Create a new item"},
            {"path": "/items/{item_id}", "method": "GET", "description": "Retrieve an item by ID"},
            {"path": "/docs", "method": "GET", "description": "API documentation"},
            {"path": "/docs/json", "method": "GET", "description": "API documentation in JSON format"}
        ]
    }
