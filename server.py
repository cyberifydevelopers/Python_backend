from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from routes import register_routes
from config.orm import TORTOISE_ORM

app = FastAPI()

register_routes(app)

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.get("/")
def root():
    return {"message": "API is running"}