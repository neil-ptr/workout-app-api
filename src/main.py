from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware


from src.routers import users, workouts
from src.database import schemas, engine

# init database
schemas.Base.metadata.create_all(bind=engine)

# TODO: change this for production
origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# other routes
app.include_router(router=users.router, prefix='/api/users')
app.include_router(router=workouts.router, prefix='/api/workouts')
