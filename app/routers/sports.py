from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=['sports'])
def list_sports():
    return {'sports': ['nba', 'nhl']}

@router.get("/{sport}", tags=['sports'])
async def get_sport_props(sport):
    return {
        'sport': sport,
        'props': []
    }

