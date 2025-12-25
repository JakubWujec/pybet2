from app.eventDispatcher import EventDispatcher
from app.games.repository import GameRepository
from app.games.score import Score


class UpdateGameScoreService:
    def __init__(
        self, gameRepository: GameRepository, eventDispatcher: EventDispatcher
    ) -> None:
        self.__gameRepository = gameRepository
        self.__eventDispatcher = eventDispatcher

    def updateScore(self, gameId: int, score: Score):
        game = self.__gameRepository.findById(gameId)

        if game is None:
            raise Exception("Game doesnt exist")

        game.updateScore(score)

        self.__gameRepository.save(game)
        self.__eventDispatcher.dispatchAll(game.releaseEvents())
