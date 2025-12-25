from pydantic import BaseModel


class Game(BaseModel):
    gameId: int
    home_side: str
    away_side: str
    kickoff: str
