from fastapi import APIRouter
from database.database import client

router = APIRouter()

@router.get('/')
def list_dfs_platforms():
    return {'dfs_platforms': ['prizepicks']}

@router.get('/{platform}')
def get_platform_props(platform):
    dfs_coll = client['props'][platform]
    props = dfs_coll.find({'dfs_platform': platform})
    return list(props)

print(get_platform_props('prizepicks'))