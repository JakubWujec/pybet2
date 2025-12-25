from pydantic import BaseModel
from sqlmodel import SQLModel, Field

from app.events import BaseEvent
from app.games.events import GameScoreUpdated
from app.games.score import Score


class Game(BaseModel):
    gameId: int
    homeSide: str
    awaySide: str
    kickoff: str
    homeSideScore: int | None = Field(default=None)
    awaySideScore: int | None = Field(default=None)

    _events: list[BaseEvent] = []

    @property
    def score(self):
        if self.homeSideScore is None or self.awaySideScore is None:
            return None
        return Score(homeSideScore=self.homeSideScore, awaySideScore=self.awaySideScore)

    def updateScore(self, score: Score):
        self.homeSideScore = score.homeSideScore
        self.awaySideScore = score.awaySideScore

        self._events.append(GameScoreUpdated(gameId=self.gameId, score=score))

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

    def toDomain(self):
        return Game.model_validate(self.model_dump())

    @classmethod
    def fromDomain(cls, game: Game):
        return cls.model_validate(game)
