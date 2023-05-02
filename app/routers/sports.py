from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_sports():
    return {'sports': ['NBA', 'NHL']}
