from app.events import BaseEvent


class GameScoreUpdated(BaseEvent):
    gameId: int
    homeSideScore: int
    awaySideScore: int
