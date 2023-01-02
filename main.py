from fastapi import FastAPI

# instanciate the framework Fast
app = FastAPI()

# the original has the async function
# app is the decoration for the endpoint
# the function root is function name
@app.get("/")
async def root():
    return {"message": "Hello World"}
