from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=['books'])
def list_books():
    return {'books': ['draftkings', 'fanduel', 'betrivers', 'pinnacle', 'pointsbet']}

@router.get("/{book}", tags=['books'])
async def get_book_props(book):
    return {
        'book': book,
        'props': []
    }