"""
API Documentation
=================

This file contains the documentation for each API endpoint.

Endpoints:
----------

1. **Root Endpoint**: `/`
   - **Method**: GET
   - **Description**: Returns a welcome message, status of the API, and a list of all available endpoints.

2. **Create Item Endpoint**: `/items/`
   - **Method**: POST
   - **Description**: Creates a new item.
   - **Request**: Expects an `Item` object.
   - **Response**: Returns the created item.

3. **Get Item by ID Endpoint**: `/items/{item_id}`
   - **Method**: GET
   - **Description**: Retrieves an item by its ID.
   - **Response**: Returns the item if found, otherwise raises a 404 error.

4. **List Items Endpoint**: `/items/`
   - **Method**: GET
   - **Description**: Lists items with pagination.
   - **Parameters**: `skip` and `limit` for pagination.
   - **Response**: Returns a list of items.

5. **API Documentation Endpoint**: `/docs`
   - **Method**: GET
   - **Description**: Provides a summary of the API endpoints.

6. **API Documentation in JSON Format**: `/docs/json`
   - **Method**: GET
   - **Description**: Provides the API documentation in JSON format.

"""
