from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends



class TaskBase(BaseModel):
    title: str
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskOut(TaskBase):
    id: int

    class Config:
        orm_mode = True


