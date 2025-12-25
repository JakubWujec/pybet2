from app.eventDispatcher import EventDispatcher
from app.games.repository import GameRepository


class UpdateGameScoreService:
    def __init__(
        self, gameRepository: GameRepository, eventDispatcher: EventDispatcher
    ) -> None:
        self.__gameRepository = gameRepository
        self.__eventDispatcher = eventDispatcher

    def updateScore(self, gameId: int, homeSideScore: int, awaySideScore: int):
        game = self.__gameRepository.findById(gameId)

        if game is None:
            raise Exception("Game doesnt exist")

        game.updateScore(homeSideScore, awaySideScore)

        self.__gameRepository.save(game)
        self.__eventDispatcher.dispatchAll(game.releaseEvents())
