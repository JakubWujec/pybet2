from app.games.repository import GameRepository


class FillGameScoreService:
    def __init__(self, gameRepository: GameRepository) -> None:
        self.__gameRepository = gameRepository

    def fillScore(self, gameId: int, homeSideScore: int, awaySideScore: int):
        game = self.__gameRepository.findById(gameId)

        if game is None:
            raise Exception("Game doesnt exist")

        game.fillScore(homeSideScore, awaySideScore)

        self.__gameRepository.save(game)
