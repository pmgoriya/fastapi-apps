from fastapi import FastAPI
from pydantic import BaseModel
from sqlmodel import SQLModel, select
from database import engine, SessionDep, Task, Status
from models import TaskCreate, TaskRead

app = FastAPI()

SQLModel.metadata.create_all(engine)


@app.get("/tasks")
async def tasks(session: SessionDep):
    tasks = session.exec(select(Task)).all()
    return tasks


@app.post("/tasks", response_model=TaskRead)
async def tasks(task: TaskCreate, session: SessionDep):
    new_task = Task(**task.model_dump(), status=Status.pending)
    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    return TaskRead.model_validate(new_task.model_dump())


# Use TaskCreate (Pydantic) for request input – no DB fields like 'id'.
# Convert input to Task (SQLModel) using task.dict(), then add → commit → refresh.
# For GET: use session.exec(select(...)) to read from DB.
# For DELETE: use session.delete(obj) → commit() to remove from DB.



# We can't return `new_task` directly because it's a SQLModel (ORM) object,
# but FastAPI expects a pure Pydantic model (`TaskRead`) as the response.
# Since Pydantic v2 doesn't auto-convert ORM objects anymore, we manually convert:
# First, we turn the SQLModel (`new_task`) into a plain dict using `.model_dump()`,
# then we pass that dict into `.model_validate()` to create a proper TaskRead instance.
