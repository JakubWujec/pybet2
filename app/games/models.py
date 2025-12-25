from pydantic import BaseModel
from sqlmodel import SQLModel, Field

from app.events import BaseEvent
from app.games.events import GameScoreFilled


class Game(BaseModel):
    gameId: int
    homeSide: str
    awaySide: str
    kickoff: str
    homeSideScore: int | None = Field(default=None)
    awaySideScore: int | None = Field(default=None)

    _events: list[BaseEvent] = []

    def fillScore(self, homeSideScore: int, awaySideScore: int):
        self.homeSideScore = homeSideScore
        self.awaySideScore = awaySideScore
        self._events.append(GameScoreFilled(gameId=self.gameId))

    def releaseEvents(self):
        events = self._events
        self._events = []
        return events


class DbGame(SQLModel, table=True):
    gameId: int = Field(default=None, primary_key=True)
    homeSide: str
    awaySide: str
    kickoff: str
    homeSideScore: int | None = Field(default=None)
    awaySideScore: int | None = Field(default=None)
