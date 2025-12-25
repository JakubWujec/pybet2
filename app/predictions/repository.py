from typing import Dict, Protocol

from app.predictions.models import Prediction


class PredictionRepository(Protocol):
    def save(self, prediction: Prediction): ...
    def getById(self, predictionId: int) -> Prediction: ...
    def getNextId(self) -> int: ...
    def findById(self, predictionId: int) -> Prediction | None: ...


class InMemoryPredictionRepository(PredictionRepository):
    def __init__(self) -> None:
        self.__predictions: Dict[int, Prediction] = {}
        self.last_id = 0

    def getNextId(self) -> int:
        self.last_id += 1
        return self.last_id

    def save(self, prediction: Prediction):
        self.__predictions[prediction.predictionId] = prediction

    def getById(self, predictionId: int):
        if predictionId not in self.__predictions:
            raise ValueError(f"No order with id {predictionId}")

        return self.__predictions[predictionId]

    def findById(self, predictionId: int):
        return self.__predictions.get(predictionId, None)
