from typing import Protocol


from app.games.score import Score
from app.predictions.models import Prediction


class PointScoring(Protocol):
    def calculatePoints(self, prediction: Prediction, score: Score) -> int: ...


class SimplePointScoring:
    def calculatePoints(self, prediction: Prediction, score: Score):
        if (
            prediction.homeSideScore == score.homeSideScore
            and prediction.awaySideScore == score.awaySideScore
        ):
            return 10

        return 0
