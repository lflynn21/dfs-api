from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import sports, books, dfs

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#app.include_router(sports.router, prefix="/sports")
#app.include_router(books.router, prefix="/books")
app.include_router(dfs.router, prefix="/dfs")

@app.get("/", tags=['root'])
def read_root():
    return "DFS Props API"