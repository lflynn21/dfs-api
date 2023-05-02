from typing import Dict, Optional
from pydantic import BaseModel

class OverUnder(BaseModel):
    over: Optional[int]
    under: Optional[int]

class PlayerLines(BaseModel):
    line: float
    books: Dict[str, OverUnder]

class Player(BaseModel):
    name: str
    stats: Dict[str, PlayerLines]