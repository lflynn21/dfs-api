from fastapi import FastAPI
from .routers import sports

app = FastAPI()

app.include_router(sports.router, prefix="/sports")

@app.get("/")
def read_root():
    return "DFS Props Api"