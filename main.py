from fastapi import FastAPI
from app import  models
from app.routers import user, role

from app.database import engine


app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(user.router)
app.include_router(role.router)
