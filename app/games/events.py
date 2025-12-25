from app.events import BaseEvent


class GameScoreFilled(BaseEvent):
    gameId: int
