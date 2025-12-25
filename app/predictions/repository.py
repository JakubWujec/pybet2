from typing import Dict, Protocol

from sqlmodel import Session

from app.predictions.models import DbPrediction, Prediction


class PredictionRepository(Protocol):
    def save(self, prediction: Prediction): ...
    def getById(self, predictionId: int) -> Prediction: ...
    def getNextId(self) -> int: ...
    def findById(self, predictionId: int) -> Prediction | None: ...


class InMemoryPredictionRepository(PredictionRepository):
    def __init__(self) -> None:
        self.__predictions: Dict[int, Prediction] = {}
        self.lastId = 0

    def getNextId(self) -> int:
        self.lastId += 1
        return self.lastId

    def save(self, prediction: Prediction):
        self.__predictions[prediction.predictionId] = prediction

    def getById(self, predictionId: int):
        if predictionId not in self.__predictions:
            raise ValueError(f"No order with id {predictionId}")

        return self.__predictions[predictionId]

    def findById(self, predictionId: int):
        return self.__predictions.get(predictionId, None)


class SqlPredictionRepository(PredictionRepository):
    def __init__(self, session: Session) -> None:
        self.lastId = 0
        self.session = session

    def getNextId(self) -> int:
        self.lastId += 1
        return self.lastId

    def save(self, prediction: Prediction):
        self.session.add(DbPrediction.model_validate(prediction))

    def getById(self, predictionId: int):
        prediction = self.session.get(DbPrediction, predictionId)
        if not prediction:
            raise ValueError(f"No prediction with id {predictionId}")

        return Prediction.model_validate(prediction.model_dump())

    def findById(self, predictionId: int):
        prediction = self.session.get(DbPrediction, predictionId)
        if prediction is None:
            return None
        return Prediction.model_validate(prediction.model_dump())
