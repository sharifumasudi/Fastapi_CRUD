from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import  models
from app.routers import user, role

from app.database import engine


app = FastAPI()

models.Base.metadata.create_all(engine)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(role.router)
