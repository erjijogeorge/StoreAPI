from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def first_root():
    return {"message": "Hello, world!"}
