from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class Game(BaseModel):
    gameId: int
    homeSide: str
    awaySide: str
    kickoff: str
    homeSideScore: int | None = Field(default=None)
    awaySideScore: int | None = Field(default=None)

    def fillScore(self, homeSideScore: int, awaySideScore: int):
        self.homeSideScore = homeSideScore
        self.awaySideScore = awaySideScore


class DbGame(SQLModel, table=True):
    gameId: int = Field(default=None, primary_key=True)
    homeSide: str
    awaySide: str
    kickoff: str
    homeSideScore: int | None = Field(default=None)
    awaySideScore: int | None = Field(default=None)
