from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.api.dependencies import get_current_user
from app.models.user import User


router = APIRouter(prefix="/api/tasks", tags=["Tasks"])


@router.get("/get", response_model=list[TaskResponse])
def get_tasks(
    db: Session = Depends(get_db),  
    current_user: User = Depends(get_current_user)
):
    """ Get all tasks for the current user. """
    
    if not current_user:
        raise HTTPException(
            status_code=401,
            detail="Authentication required"
        )

    tasks = db.query(Task)

    return tasks

@router.post("/create", response_model=TaskResponse, status_code=201)
def create_task(
    task_data: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """ Create a new task. """
    
    if not current_user:
        raise HTTPException(
            status_code=401,
            detail="Authentication required"
        )
    
    assigned_user = db.get(User, task_data.user_id)
    if assigned_user is None:
        raise HTTPException(
            status_code=404,
            detail="Assigned user not found"
        )

    task = Task(
        **task_data.model_dump(exclude={"user_id"}),
        user_id=assigned_user.id,
    )



    db.add(task)
    db.commit()
    db.refresh(task)

    return task


@router.put("/update/{task_id}", response_model=TaskResponse)
def update_task(
    task_id:int,
    task_data: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not current_user:
        raise HTTPException(
            status_code=401,
            detail="Authentication required"
        )

    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    for key, value in task_data.model_dump(exclude_unset=True).items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)

    return task

@router.delete("/delete/{task_id}", status_code=204)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not current_user:
        raise HTTPException(
            status_code=401,
            detail="Authentication required"
        )

    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(task)
    db.commit()

    return {
        "message": "Task deleted successfully"
    }