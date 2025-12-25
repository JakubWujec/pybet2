from fastapi.testclient import TestClient
from sqlmodel import Session
from app.games.models import DbGame


class TestMakePredictionEndpoint:
    def test_make_first_prediction(self, session: Session, client: TestClient):
        game1 = DbGame(
            gameId=1,
            home_side="Arsenal",
            away_side="Spurs",
            kickoff="2027-12-24 11:30",
        )
        session.add(game1)
        session.commit()

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
