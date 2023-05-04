from typing import Dict, Optional
from pydantic import BaseModel

class BookOdds(BaseModel):
    odds: int
    implied_percentage: float

class Player(BaseModel):
    id: int
    name: str
    display_name: str
    position: str
    opponent: str
    line_score: float
    stat_type: str
    team: str
    league: str
    bet_type: str
    comp_percent: float
    dfs_book: str
    active: bool
    books: Dict[str, BookOdds]