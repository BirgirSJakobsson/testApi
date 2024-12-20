# TestAPI

A simple REST API built with FastAPI.

## Features
- FastAPI framework for high performance
- Automatic API documentation
- Type hints and validation
- RESTful endpoints

## Setup

1. Create a virtual environment:
```bash
python3 -m venv venv
```

2. Activate the virtual environment:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Run the server:
```bash
uvicorn main:app --reload
```

5. Access the API:
- API endpoints: http://localhost:8000
- Interactive documentation: http://localhost:8000/docs
- OpenAPI specification: http://localhost:8000/openapi.json

## API Endpoints

### Welcome Endpoint
```bash
curl http://localhost:8000/
```

### Create Item
```bash
curl -X POST http://localhost:8000/items/ -H "Content-Type: application/json" -d '{"name": "Test Item", "description": "This is a test item", "price": 29.99, "is_available": true}'
```

### Get All Items
```bash
curl http://localhost:8000/items/
```

### Get Item by ID
```bash
curl http://localhost:8000/items/1
```

## Docker Commands

### Build and Run the Docker Container
```bash
docker build -t testapi .
docker run -p 8000:8000 -v ${PWD}/test.db:/app/test.db --name testapi-container testapi
```

### Reload the Docker Container
You can use the following script to stop, remove, build, and run the Docker container:
```bash
dockerReload.bat
```

## Notes
- Ensure Docker is running before executing Docker commands.
- Modify the [dockerReload.bat](cci:7://file:///c:/Users/Chirno/CascadeProjects/TestApi/Utils/Scripts/dockerReload.bat:0:0-0:0) script as needed for your environment.
- Setting the Variable:
   When you run your application or Docker container, you can set the APP_ENV variable in different ways:
   In the Terminal:
   bash
   CopyInsert in Terminal
   $env:APP_ENV="production"
   This command sets the APP_ENV variable to production for the current terminal session. You can then run your application, and it will load the .env.production file.
   In Docker: When running your Docker container, you can set the environment variable using the -e flag:
   bash
   CopyInsert in Terminal
   docker run -e APP_ENV=production -p 8000:8000 myfastapiapp
   This command sets the APP_ENV variable to production for the container, allowing it to load the appropriate configuration.



# Create the volume for PostgreSQL
docker volume create pg_data

# Run the PostgreSQL container
docker run -d \
    --name postgres_container \
    -e POSTGRES_USER=testapidev \
    -e POSTGRES_PASSWORD=testapidevpass \
    -e POSTGRES_DB=testapidb \
    -v pg_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres:latest

# test 
docker run --name postgres-container -e POSTGRES_PASSWORD=pw -d -v pgdata:/var/lib/postgresql/data postgres