from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import users, workouts

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=users.router, prefix='/api')
app.include_router(router=workouts.router, prefix='/api')
