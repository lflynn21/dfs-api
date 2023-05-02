from fastapi import FastAPI
from .database import client
from .main import router as main_router


app = FastAPI()

app.include_router(main_router, prefix='/api')

# @app.on_event('startup')
# async def startup():
#     await client.connect()

# @app.on_event('shutdown')
# async def shutdown():
#     await client.disconnect()