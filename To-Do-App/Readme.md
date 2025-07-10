### To-do App
A simple Restful API to create, read, update, and delete personal tasks

### Project Objectives
- practice fast-api fundamentals (CRUD ops, SQLite, Pydantic Models)
- clean api design and follow the best practices.

### Endpoints Overview
| Method | Endpoint | Description|
|--------|----------|----------------------|
| GET | /tasks | Get all tasks |
| GET | /tasks/{id} | Get a task by id |
| POST | /tasks | Create a new task |
| PUT | /tasks/{id} | Update a task |
| DELETE | /tasks/{id} | Delete a task |


### Data Models
Task Model:
- id: integer (auto generated)
- title: string (required)
- description: string (optional)
- status: enum -> pending | in-progress | completed


### Tech Stack
- FastAPI for routing and request handling
- Pydantic for data validation
- sqlalchemy as ORM
- sqlite for lightweight db
- uvicorn for asgi server


### Running instructions