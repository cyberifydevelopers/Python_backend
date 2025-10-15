import os
from dotenv import load_dotenv

load_dotenv()
DB_URL = os.getenv("DB_URL")

TORTOISE_ORM = {
    "connections": {"default": DB_URL},
    "apps": {
        "models": {
            "models": ["models.user", "models.tasks", 'aerich.models'],
            "default_connection": "default",
        },
    },
}