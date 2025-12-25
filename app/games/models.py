from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class Game(BaseModel):
    gameId: int
    homeSide: str
    awaySide: str
    kickoff: str
    homeSideScore: int | None = Field(default=None)
    awaySideScore: int | None = Field(default=None)


class DbGame(SQLModel, table=True):
    gameId: int = Field(default=None, primary_key=True)
    homeSide: str
    awaySide: str
    kickoff: str
    homeSideScore: int | None = Field(default=None)
    awaySideScore: int | None = Field(default=None)
