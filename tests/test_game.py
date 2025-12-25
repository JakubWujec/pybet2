from app.games.events import GameScoreFilled
from app.games.models import Game


class TestGame:
    def test_filling_score_release_event(self):
        game = Game(gameId=1, homeSide="A", awaySide="B", kickoff="2027-12-24 11:30")
        game.fillScore(2, 3)

        events = game.releaseEvents()

        assert len(events) > 0
        assert GameScoreFilled(gameId=game.gameId) in events
