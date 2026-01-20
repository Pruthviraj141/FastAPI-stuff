from fastapi import HTTPException
from src.tasks.dtos import TaskSchema, TaskUpdateSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel

def create_task(body:TaskSchema,db:Session):
    data = body.model_dump()
    newtask = TaskModel(title=data['title'],
                        description=data['description'],
                        is_completed=data['is_completed'])
    db.add(newtask)
    db.commit()
    db.refresh(newtask)
    return newtask

def get_tasks(db:Session):
    tasks = db.query(TaskModel).all()
    return tasks

def get_task_by_id(task_id:int,db:Session):
    task = db.query(TaskModel).get(task_id)
    return {"status":"success","data":task}


def update_task(task_id:int, body:TaskUpdateSchema, db:Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    # one_task.title = body.title
    # one_task.description = body.description  
    # more effective way to write this is that
    body = body.model_dump(exclude_unset=True, exclude_none=True) # only fields provided by client
    for key,value in body.items():
        setattr(one_task,key,value) 
    
    db.add(one_task)
    db.commit()
    db.refresh(one_task)
    return {"status":"success","data":one_task}


def delete_task(task_id:int, db:Session): 
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(one_task)
    db.commit()
    #insted of returning data we can just return status code which is more professional 
    return None
