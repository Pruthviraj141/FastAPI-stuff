from fastapi import FastAPI
from src.utils.db import Base, engine
from src.tasks.models import TaskModel
from src.tasks.router import task_router



Base.metadata.create_all(bind=engine)  # Comment this out after initial setup


app =  FastAPI(title="Task Manager")
app.include_router(task_router)

