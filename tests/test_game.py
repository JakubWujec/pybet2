from app.games.events import GameScoreUpdated
from app.games.models import Game
from app.games.score import Score


class TestGame:
    def test_updating_score_release_event(self):
        game = Game(gameId=1, homeSide="A", awaySide="B", kickoff="2027-12-24 11:30")
        score = Score(homeSideScore=2, awaySideScore=3)

        game.updateScore(score)

        events = game.releaseEvents()

        assert len(events) > 0
        assert GameScoreUpdated(gameId=game.gameId, score=score) in events
