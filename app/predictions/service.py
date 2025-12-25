from pydantic import BaseModel
from app.games.events import GameScoreUpdated
from app.games.repository import GameRepository
from app.predictions.exceptions import CouldNotCreatePrediction
from app.predictions.models import Prediction
from app.predictions.repository import PredictionRepository


class MakePrediction(BaseModel):
    gameId: int
    homeSideScore: int
    awaySideScore: int


class MakePredictionService:
    def __init__(
        self, gameRepository: GameRepository, predictionRepository: PredictionRepository
    ) -> None:
        self.__gameRepository = gameRepository
        self.__predictionRepository = predictionRepository

    def make(self, makePrediction: MakePrediction) -> int:
        game = self.__gameRepository.findById(makePrediction.gameId)
        if game is None:
            raise CouldNotCreatePrediction.becauseGameDoesNotExist()

        nextId = self.__predictionRepository.getNextId()

        self.__predictionRepository.save(
            Prediction(
                predictionId=nextId,
                gameId=makePrediction.gameId,
                homeSideScore=makePrediction.homeSideScore,
                awaySideScore=makePrediction.awaySideScore,
            )
        )

        return nextId


class UpdatePredictionPointsService:
    def __init__(self, predictionRepository: PredictionRepository) -> None:
        self.__predictionRepository = predictionRepository

    def updatePredictionsFor(self, gameId: int, homeSideScore: int, awaySideScore: int):
        predictions = self.__predictionRepository.getRelatedTo(gameId)
        for prediction in predictions:
            prediction.updatePoints(
                self.calculatePoints(prediction, homeSideScore, awaySideScore)
            )
        self.__predictionRepository.saveAll(predictions)

    def calculatePoints(
        self, prediction: Prediction, homeSideScore: int, awaySideScore: int
    ):
        return 5


class UpdatePredictionPoints:
    def __init__(self, service: UpdatePredictionPointsService) -> None:
        self.__service = service

    def whenGameScoreUpdated(self, event: GameScoreUpdated):
        self.__service.updatePredictionsFor(
            event.gameId, event.homeSideScore, event.awaySideScore
        )
