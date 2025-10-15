from tortoise import fields
from .base import BaseModel

class Tasks(BaseModel):
    title = fields.CharField(max_length=255, null=False)
    description = fields.TextField(null=False)
    createby = fields.IntField()  # User ID who created the task
    isCompleted = fields.BooleanField(default=False)

    class Meta:
        table = "tasks"