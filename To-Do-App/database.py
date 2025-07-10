
from sqlmodel import create_engine, Session, SQLModel, Field
from typing import Annotated
from fastapi import Depends
from enum import Enum


class Status(str, Enum):
    pending = "pending"
    inprogress = "in-progress"
    completed = "completed"

class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str | None
    status: Status




sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
