from fastapi import APIRouter
from app.database.database import *
from app.models.models import *

router = APIRouter()

@router.get('/', tags=['dfs'])
def list_dfs_platforms():
    return {'dfs_platforms': ['prizepicks']}

@router.get('/{platform}', tags=['dfs'])
async def get_active_platform_props(platform, league=None) -> list[Player]:
    return get_active_props(platform, league)

