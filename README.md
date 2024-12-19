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
