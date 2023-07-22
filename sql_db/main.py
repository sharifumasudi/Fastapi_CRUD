from fastapi import FastAPI
from datetime import datetime
from . import schemas, models

from .database import engine


app = FastAPI()

models.Base.metadata.create_all(engine)

@app.get("/")
async def index():
    return {"data": {"name": "Sharifu", "email": "sharifumasudi66@gmail.com", "created_at": datetime.now()}}

@app.post("/user")
async def create(request: schemas.User):
    return request

@app.delete("/user/{id}")
async def delete(id: str):
    return id

@app.put("/user/{id}")
async def update(id: int):
    return id