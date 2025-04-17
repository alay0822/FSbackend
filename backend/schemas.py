from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends

class TaskBase(BaseModel):
    title: str
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None

class TaskOut(TaskBase):
    id: int

    class Config:
        from_attributes = True


