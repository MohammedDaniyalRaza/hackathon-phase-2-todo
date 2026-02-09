# API Documentation

## Authentication Endpoints

### Register User
- **Endpoint**: `POST /v1/auth/register`
- **Description**: Creates a new user account with email and password
- **Request Body**:
  ```json
  {
    "email": "string",
    "password": "string"
  }
  ```
- **Response**: User object with 201 status code
- **Errors**: 409 Conflict if email already exists

### Login User
- **Endpoint**: `POST /v1/auth/login`
- **Description**: Authenticates user with email and password, returns JWT token
- **Request Body**:
  ```json
  {
    "email": "string",
    "password": "string"
  }
  ```
- **Response**: 
  ```json
  {
    "access_token": "string",
    "token_type": "bearer"
  }
  ```
- **Errors**: 401 Unauthorized if credentials are invalid

### Logout User
- **Endpoint**: `POST /v1/auth/logout`
- **Description**: Revokes the current user session
- **Authentication**: Requires Bearer token
- **Response**: Success message

## Task Management Endpoints

### Get All Tasks
- **Endpoint**: `GET /v1/tasks`
- **Description**: Returns a list of tasks owned by the authenticated user
- **Authentication**: Requires Bearer token
- **Response**: Array of Task objects

### Create Task
- **Endpoint**: `POST /v1/tasks`
- **Description**: Creates a new task for the authenticated user
- **Authentication**: Requires Bearer token
- **Request Body**:
  ```json
  {
    "title": "string",
    "description": "string",
    "completed": "boolean"
  }
  ```
- **Response**: Created Task object

### Get Task by ID
- **Endpoint**: `GET /v1/tasks/{taskId}`
- **Description**: Returns details of a specific task owned by the authenticated user
- **Authentication**: Requires Bearer token
- **Response**: Task object
- **Errors**: 404 Not Found if task doesn't exist

### Update Task
- **Endpoint**: `PUT /v1/tasks/{taskId}`
- **Description**: Updates details of a specific task owned by the authenticated user
- **Authentication**: Requires Bearer token
- **Request Body**:
  ```json
  {
    "title": "string",
    "description": "string",
    "completed": "boolean"
  }
  ```
- **Response**: Updated Task object
- **Errors**: 404 Not Found if task doesn't exist

### Delete Task
- **Endpoint**: `DELETE /v1/tasks/{taskId}`
- **Description**: Deletes a specific task owned by the authenticated user
- **Authentication**: Requires Bearer token
- **Response**: Success message
- **Errors**: 404 Not Found if task doesn't exist