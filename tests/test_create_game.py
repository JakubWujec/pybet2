from fastapi.testclient import TestClient


class TestGameEndpoint:
    def test_create_first_game(self, client: TestClient):
        response = client.post(
            "/games/",
            json={
                "home_side": "Arsenal",
                "away_side": "Spurs",
                "kickoff": "2027-12-24 11:30",
            },
        )

        assert response.status_code == 200
        assert response.json() == {"gameId": 1}

    def test_get_created_game(self, client):
        client.post(
            "/games/",
            json={
                "home_side": "Arsenal",
                "away_side": "Spurs",
                "kickoff": "2027-12-24 11:30",
            },
        )

        response = client.get("/games/1")

        assert response.status_code == 200
        assert response.json() == {
            "game": {
                "gameId": 1,
                "home_side": "Arsenal",
                "away_side": "Spurs",
                "kickoff": "2027-12-24 11:30",
            }
        }
