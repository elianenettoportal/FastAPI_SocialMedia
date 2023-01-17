from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import post, user, auth, vote
from sqlalchemy_utils import database_exists, create_database
from . import utils

# Note: SQLAlchemy will see if tables exists, if not it creates
utils.database_exists()

# instanciate the framework Fast
app = FastAPI()

# List of domains that can talk to this API. * will allow all
origins = ["*"]

# A middleware is a function that executes before any request. Before going to each of the routers below, the middleware will perform changes
# We want to allow access from other domains access since CORS is blocked by javascript
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Healthy!!!!!"}
