from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str
    createby: int  # User ID who created the task
    isCompleted: bool = False

