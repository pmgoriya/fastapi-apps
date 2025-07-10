from fastapi import FastAPI
from pydantic import BaseModel

# class Status(str, Enum):
#     pending = "pending"
#     inprogress = "in-progress"
#     completed = "completed"

# class Task(BaseModel):
#     title: str
#     description: str | None
#     status: Status



app = FastAPI()


@app.get("/tasks")
async def tasks():
    return {"message": "These are my tasks"}