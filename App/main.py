from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# uncomment in case you want to run the base models creation
from .database import engine
from . import models
from .routers import post, user, auth, vote

# SQLAlchemy will see if tables exists, if not it creates
# Note: If first access uncomment belolow
models.Base.metadata.create_all(bind=engine)

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