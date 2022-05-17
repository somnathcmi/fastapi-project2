from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "This is root of FastAPI webapi deployed on deta by somnath"

@app.get("/info")
async def root():
    return {"message": "Hello World"}
