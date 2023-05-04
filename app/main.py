from fastapi import FastAPI
from .routers import sports, books, dfs

app = FastAPI()

app.include_router(sports.router, prefix="/sports")
app.include_router(books.router, prefix="/books")
app.include_router(dfs.router, prefix="/dfs")

@app.get("/", tags=['root'])
def read_root():
    return "DFS Props API"