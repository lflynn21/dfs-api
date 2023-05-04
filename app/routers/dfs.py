from fastapi import APIRouter
from app.database.database import *

router = APIRouter()

@router.get('/')
def list_dfs_platforms():
    return {'dfs_platforms': ['prizepicks']}

@router.get('/{platform}')
async def get_platform_props(platform, league=None):
    return get_active_props(platform, league)

