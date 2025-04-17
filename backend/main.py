from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from backend import models, database, schemas, crud
from backend.database import Base, SessionLocal

models.Base.metadata.create_all(bind=database.engine)

db = SessionLocal()
print(db.query(models.Task).all())

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/tasks/", response_model=list[schemas.TaskOut])
def read_tasks(completed: bool | None = None, db: Session = Depends(get_db)):
    if completed is None:
        return crud.get_tasks(db)
    return crud.get_tasks_by_status(db, completed)

@app.post("/api/tasks/", response_model=schemas.TaskOut)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@app.get("/api/tasks/{task_id}/", response_model=schemas.TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/api/tasks/{task_id}/", response_model=schemas.TaskOut)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    return crud.update_task(db, task_id, task)

@app.delete("/api/tasks/{task_id}/")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return crud.delete_task(db, task_id)

@app.delete("/api/tasks/")
def delete_all_tasks(db: Session = Depends(get_db)):
    crud.delete_all_tasks(db)
    return {"detail": "All tasks deleted"}
