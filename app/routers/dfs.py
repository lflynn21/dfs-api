from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def list_dfs_platforms():
    return {'dfs_platforms': ['prizepicks']}

@router.get('/{platform}')
async def get_platform_props(platform):
    return {
        'dfs_platform': platform,
        'props': []
    }