from fastapi import APIRouter, HTTPException, status, Depends
from tortoise.exceptions import DoesNotExist
import os
from dotenv import load_dotenv
from schemas.tasks import TaskCreate
from models.user import User
from models.tasks import Tasks
from controllers.deps import get_current_user
load_dotenv()
router = APIRouter()


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


@router.post("/create-task")
async def create_task(task: TaskCreate, current_user: User = Depends(get_current_user)):
    task_obj = await Tasks.create(
        title=task.title,
        description=task.description,
        createby=current_user,
        isCompleted=task.isCompleted
    )
    return {
        "status": "success",
        "data": {
            "id": task_obj.id,
            "title": task_obj.title,
            "description": task_obj.description,
            "isCompleted": task_obj.isCompleted,
            "createby": current_user.username
        }
    }