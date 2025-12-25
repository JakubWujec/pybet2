from typing import Dict, Protocol

from fastapi import Depends
from sqlmodel import Session

from app.db_session import get_session
from app.games.models import DbGame, Game


class GameRepository(Protocol):
    def save(self, game: Game): ...
    def getById(self, gameId: int) -> Game: ...
    def getNextId(self) -> int: ...
    def findById(self, gameId: int) -> Game | None: ...


class InMemoryGameRepository(GameRepository):
    def __init__(self) -> None:
        self.__games: Dict[int, Game] = {}
        self.last_id = 0

    def getNextId(self) -> int:
        self.last_id += 1
        return self.last_id

    def save(self, game: Game):
        self.__games[game.gameId] = game

    def getById(self, gameId: int):
        if gameId not in self.__games:
            raise ValueError(f"No order with id {gameId}")

        return self.__games[gameId]

    def findById(self, gameId: int):
        return self.__games.get(gameId, None)


class SqlGameRepository(GameRepository):
    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session

    def getNextId(self) -> int:
        self.last_id += 1
        return self.last_id

    def save(self, game: Game):
        self.session.add(DbGame.model_validate(game))

    def getById(self, gameId: int):
        game = self.session.get(DbGame, gameId)
        if not game:
            raise ValueError(f"No order with id {gameId}")

        return Game.model_validate(game)

    def findById(self, gameId: int):
        game = self.session.get(DbGame, gameId)
        return Game.model_validate(game)
