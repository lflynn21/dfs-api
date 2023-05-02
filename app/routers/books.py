from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_books():
    return {'books': ['draftkings', 'fanduel', 'betrivers', 'pinnacle', 'pointsbet']}

@router.get("/{book}")
async def get_book_props(book):
    return {
        'book': book,
        'props': []
    }