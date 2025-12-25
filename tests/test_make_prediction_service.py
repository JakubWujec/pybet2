import pytest
from app.games.repository import InMemoryGameRepository
from app.predictions.exceptions import CouldNotCreatePrediction
from app.predictions.repository import InMemoryPredictionRepository
from app.predictions.service import MakePrediction, MakePredictionService


class TestMakePredictionService:
    def test_raise_exception_when_game_doesnt_exist(self):
        gameRepo = InMemoryGameRepository()
        predictionRepo = InMemoryPredictionRepository()
        service = MakePredictionService(gameRepo, predictionRepo)

        with pytest.raises(CouldNotCreatePrediction):
            service.make(
                MakePrediction(
                    gameId=1,
                    homeSideScore=1,
                    awaySideScore=1,
                )
            )
