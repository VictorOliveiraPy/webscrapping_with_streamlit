from fastapi import FastAPI

from controller.route import item_router

app = FastAPI()


@app.get("/")
async def pong():
    return {"Ping": "Pong"}


app.include_router(item_router, prefix="/items")
