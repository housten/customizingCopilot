# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement RESTful APIs using the FastAPI framework in Python. You will create a simple API for managing a collection of resources, practicing endpoint creation, request handling, and response formatting.

## 📝 Tasks

### 🛠️	Set Up FastAPI Project

#### Description
Initialize a new FastAPI project and set up the basic structure for your API application.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn
- Create a main application file (e.g., main.py)
- Set up a basic FastAPI app and run it locally


### 🛠️	Create CRUD Endpoints

#### Description
Implement RESTful endpoints to Create, Read, Update, and Delete (CRUD) items in your API.

#### Requirements
Completed program should:

- Define a Pydantic model for your resource (e.g., Item)
- Implement endpoints for:
  - Creating a new item (POST)
  - Retrieving all items (GET)
  - Retrieving a single item by ID (GET)
  - Updating an item by ID (PUT or PATCH)
  - Deleting an item by ID (DELETE)
- Return appropriate status codes and JSON responses


### 🛠️	(Optional) Add Extra Features

#### Description
Enhance your API with additional features for better usability and robustness.

#### Requirements
Completed program could:

- Add input validation and error handling
- Implement filtering or searching
- Add OpenAPI documentation customization
- Write example requests using curl or httpie
