from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import strawberry
from strawberry.asgi import GraphQL

from src.middleware import catch_exceptions_middleware
from src.routers import auth
from src.database import schemas, engine
from src.graphql import Query, Mutation

# init database
schemas.Base.metadata.create_all(bind=engine)

# TODO: change this for production
origins = [
    "http://localhost",
    "https://localhost",
    "http://localhost:3000",
    "https://localhost:3000",
]

app = FastAPI()

app.middleware('http')(catch_exceptions_middleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQL(schema)

app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)

# other routes
app.include_router(router=auth.router, prefix='/api/auth')
