from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class Game(BaseModel):
    gameId: int
    home_side: str
    away_side: str
    kickoff: str


class DbGame(SQLModel, table=True):
    gameId: int | None = Field(default=None, primary_key=True)
    home_side: str
    away_side: str
    kickoff: str
