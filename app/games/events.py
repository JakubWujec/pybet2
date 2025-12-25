from app.events import BaseEvent
from app.games.score import Score


class GameScoreUpdated(BaseEvent):
    gameId: int
    score: Score
