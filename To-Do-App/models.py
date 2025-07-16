from pydantic import BaseModel
from database import Status

class TaskCreate(BaseModel):
    title: str
    description: str | None
    # status: Status = Status.pending

class TaskRead(BaseModel):
    id: int
    title: str
    description: str | None
    status: Status

