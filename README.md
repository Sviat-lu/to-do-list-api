[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![FastAPI](https://img.shields.io/badge/framework-FastAPI-green)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/database-PostgreSQL-blue)](https://www.postgresql.org/)
[![orm](https://img.shields.io/badge/orm-SQLAlchemy-red)](https://www.sqlalchemy.org/)
[![Black](https://img.shields.io/badge/codestyle-black-black)](https://github.com/psf/black)

# To Do Task Tracker Backend

This project represents the backend of a "To Do" service for task tracking, built using FastAPI and PostgreSQL/MySQL. The application provides a set of RESTful API endpoints to create, retrieve, update, and list tasks, with JWT-based authentication for secure access.

## Table of Contents

- [Overview](#overview)
- [Technologies](#technologies)
- [Features](#features)
- [Installation](#installation)
  - [Using Docker](#using-docker)
  - [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [License](#license)

## Overview

This is a backend service for a simple To Do application. It allows users to manage tasks by creating, updating, retrieving, and listing tasks. Each task contains essential information such as a due date, task description, and timestamps for creation and updates. The project is containerized using Docker, and the configuration is handled via environment variables.

## Technologies

- **Language**: Python 3.12
- **Framework**: FastAPI 0.115.0
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Containerization**: Docker
- **Authentication**: JWT

## Features

1. **Task Management**:
   - Create tasks with a due date and description.
   - Retrieve task details by ID.
   - Update task information.
   - List all tasks with their due dates and descriptions.
   - Delete task by ID.

2. **API Documentation**:
   - Integrated Swagger UI for easy API exploration.

3. **JWT Authentication**:
   - All API endpoints are protected by JWT tokens for secure access.

## Installation

To run the project locally, follow the steps below.

### Using Docker

1. Clone the repository:

   ```bash
   git clone https://github.com/Sviat-lu/to-do-list-api
   cd to-do-list
   ```

2. Set up environment variables in `.env.template`:

   ```bash
   POSTGRES_DB="your_db_name_here"
   POSTGRES_USER="your_db_user_here"
   POSTGRES_PASSWORD="your_password_here"

   JWT_SECRET_KEY="your_secret_key_here"
   ```

3. Start the application using script:

   ```bash
   source scripts/start.sh
   ```

This will start the FastAPI server and the PostgreSQL database.

4. Access the application:

   **FastAPI docs**: http://localhost:8000/docs

   **OpenAPI schema**: http://localhost:8000/openapi.json


### Setup Instructions:

> **Prerequisites:**
> - **Python 3.12+**
> - **PostgreSQL 15.8+**
> - **Poetry** (for dependency management)

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Sviat-lu/to-do-list-api
   cd to-do-list
   ```
2. **Set Up the Virtual Environment:**

   ```bash
   poetry install

3. **Create a `.env` file in the root directory and add the following variables:**

    ```bash
    PYTHONPATH=./src

    APP_HOST="0.0.0.0"
    APP_PORT=8000

    POSTGRES_HOST="127.0.0.1"
    POSTGRES_PORT=5432
    POSTGRES_DB="your_db_name_here"
    POSTGRES_USER="your_db_user_here"
    POSTGRES_PASSWORD="your_password_here"

    JWT_SECRET_KEY="your_secret_key_here"
    JWT_ACCESS_TOKEN_EXPIRES=6000 # minutes

    ```

4. **Create new db table using command:**
    ```bash
    psql -U %your_db_user_here% -d %your_password_here% -f ./docker/initdb/init.sql
    ```

5. **Run server:**
    ```bash
    python3 main.py
    ```

6. **Access the application:**

   **FastAPI docs**: http://localhost:8000/docs

   **OpenAPI schema**: http://localhost:8000/openapi.json


## API Endpoints

### The following API endpoints are available:

- **Create Task**:
  `POST /v1/tasks/`
  Creates a new task in the database.

  **Request Body**:
  ```json
  {
    "date_to_do": "2024-12-31T23:59:59.099Z",
    "task_info": "string"
  }
   ```

  **Response**:
  ```json
  {
    "date_to_do": "2024-12-31T23:59:59.099Z",
    "task_info": "string"
  }
   ```

- **Get Task by ID**:
  `GET /v1/tasks/{task_id}/`
  Retrieves the details of a specific task by its ID.

  **Response**:
  ```json
  {
    "date_to_do": "2024-12-31T23:59:59.099Z",
    "task_info": "string"
  }
   ```

- **Update Task**:
  `PATCH /v1/tasks/{task_id}/`
   Updates the task information. The updated_at field will be automatically updated.

  **Request Body (at least one field is required)**:
  ```json
  {
    "task_info": "Updated task description"
  }
   ```

  **Response**:
  ```json
  {
    "date_to_do": "2024-12-31T23:59:59.099Z",
    "task_info": "Updated task description"
  }
   ```

- **List All Tasks**:
  `GET /v1/tasks/`
   Retrieves a list of all tasks, including their due dates and descriptions.

  **Response**:
  ```json
  [
     {
        "date_to_do": "2024-12-31T23:59:59.099Z",
        "task_info": "task_1"
     },
     {
        "date_to_do": "2024-12-31T23:59:59.099Z",
        "task_info": "task_2"
     }
  ]
   ```

- **Remove Task**:
  `DELETE /v1/tasks/{task_id}/`
   Remove task from the database by its ID.


## Authentication

This application uses cookie-based authentication, where a JWT token is stored in the user's cookies upon login and removed upon logout. The following authentication-related endpoints are provided:

- **Login**:
  `GET /v1/auth/login/`
  This endpoint handles user login by setting an authentication token in the response cookies. The token is then used to authorize subsequent requests to protected endpoints.

  **Request**:
  No request body required.

  **Response**:
  On successful login, a JWT token is stored in the cookies:
  - HTTP Status Code: `200 OK`
  - JWT Token: Stored in cookies as `Authorization` cookie

- **Logout**:
  `GET /v1/auth/logout/`
    This endpoint handles user logout by removing the authentication token from the response cookies. This action revokes the user's authentication and prevents further access to protected endpoints.

  **Request**:
  No request body required.

  **Response**:
  - HTTP Status Code: `200 OK`
  - The Authorization cookie is cleared.


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
