## here we defined the routs for all of the data
from fastapi import APIRouter, HTTPException,Depends,status
from src.tasks import controller
from src.tasks.dtos import TaskSchema, TaskUpdateSchema,TaskResponseSchema
from typing import List
from src.utils.db import get_db
from sqlalchemy.orm import Session  

task_router = APIRouter(prefix="/tasks")

@task_router.post("/create",response_model=TaskResponseSchema,status_code=status.HTTP_201_CREATED)
def create_task(body: TaskSchema,db: Session = Depends(get_db)):
    return controller.create_task(body,db) 


@task_router.get("/all",response_model=List[TaskResponseSchema],status_code=status.HTTP_200_OK)
def get_tasks(db: Session = Depends(get_db)):
    return controller.get_tasks(db)



@task_router.get("/one/{task_id}",response_model=TaskResponseSchema,status_code=status.HTTP_200_OK)
def get_task_by_id(task_id:int,db: Session = Depends(get_db)):
    one_task = db.query(controller.TaskModel).get(task_id)    
    if not one_task:
            raise HTTPException(status_code=400,detail="Task ID is required")
    return {"status":"success","data":one_task}


@task_router.put("/update/{task_id}",response_model=TaskResponseSchema,status_code=status.HTTP_200_OK)
def update_task(task_id:int, body:TaskUpdateSchema, db: Session = Depends(get_db)):
    return controller.update_task(task_id,body,db)

@task_router.delete("/delete/{task_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int, db: Session = Depends(get_db)):
    return controller.delete_task(task_id,db)