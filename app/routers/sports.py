from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_sports():
    return {'sports': ['nba', 'nhl']}

@router.get("/{sport}")
async def get_sport_props(sport):
    return {
        'sport': sport,
        'props': []
    }

