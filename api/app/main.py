from fastapi import FastAPI, HTTPException
from app.models import Task, TaskCreate
from app import storage

app = FastAPI(title="TaskFlow API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(payload: TaskCreate):
    task = Task.new(payload)
    storage.save(task)
    # Aquí, más adelante, encolaremos el task_id en SQS para que el worker lo procese
    return task


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    return storage.list_all()


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str):
    task = storage.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
