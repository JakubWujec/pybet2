import pytest
from app.dependencies import get_game_repository
from app.games.models import Game
from app.games.repository import InMemoryGameRepository
from app.main import app
from fastapi.testclient import TestClient


class TestMakePredictionEndpoint:
    @pytest.fixture(scope="class")
    def test_game_repository(self):
        repo = InMemoryGameRepository()
        repo.save(
            Game(
                gameId=1,
                home_side="Arsenal",
                away_side="Spurs",
                kickoff="2027-12-24 11:30",
            )
        )
        return repo

    @pytest.fixture(scope="class")
    def client(
        self,
    ):
        test_app = app
        test_app.dependency_overrides[get_game_repository] = self.test_game_repository

        return TestClient(test_app)

    def test_make_first_prediction(self, client):
        response = client.post(
            "/predictions/",
            json={
                "gameId": 1,
                "homeSideScore": 1,
                "awaySideScore": 1,
            },
        )

        assert response.status_code == 200
        assert response.json() == {"predictionId": 1}
