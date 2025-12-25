from app.games.models import Game
from app.games.repository import InMemoryGameRepository
from app.games.services import FillGameScoreService


class TestFillGameScoreService:
    def test_fill_game_score_change_score_to_provided_values(self):
        gameRepo = InMemoryGameRepository()
        service = FillGameScoreService(gameRepo)

        game1 = Game(
            gameId=1,
            homeSide="Arsenal",
            awaySide="Spurs",
            kickoff="2027-12-24 11:30",
        )
        gameRepo.save(game1)

        service.fillScore(gameId=1, homeSideScore=1, awaySideScore=1)

        game = gameRepo.getById(1)

        assert game.homeSideScore == 1
        assert game.awaySideScore == 1
