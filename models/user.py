from tortoise import fields
from .base import BaseModel

class User(BaseModel):
    firstName = fields.CharField(max_length=50, null=False)
    lastName = fields.CharField(max_length=50, null=False)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=255, unique=True)
    hashed_password = fields.CharField(max_length=255)

    class Meta: 
        table = "users"