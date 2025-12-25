from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from app.eventDispatcher import SimpleEventDispatcher
from app.predictions.pointScoring import PointScoring, SimplePointScoring
from app.registerEventSubscribers import registerEventSubscribers
from app.db_session import get_session
from app.games.repository import (
    GameRepository,
    SqlGameRepository,
)
from app.predictions.repository import (
    PredictionRepository,
    SqlPredictionRepository,
)
from app.predictions.service import (
    MakePredictionService,
    UpdatePredictionPoints,
    UpdatePredictionPointsService,
)


def get_game_repository(session: Annotated[Session, Depends(get_session)]):
    return SqlGameRepository(session)


def get_prediction_repository(session: Annotated[Session, Depends(get_session)]):
    return SqlPredictionRepository(session)


def getPointScoring() -> PointScoring:
    return SimplePointScoring()


def getMakePredictionService(
    gameRepository: Annotated[GameRepository, Depends(get_game_repository)],
    predictionRepository: Annotated[
        PredictionRepository, Depends(get_prediction_repository)
    ],
):
    return MakePredictionService(gameRepository, predictionRepository)


def getUpdatePredictionPoints(
    predictionRepository: Annotated[
        PredictionRepository, Depends(get_prediction_repository)
    ],
    pointScoring: Annotated[PointScoring, Depends(getPointScoring)],
):
    updatePredictionPointsService = UpdatePredictionPointsService(
        predictionRepository, pointScoring
    )
    return UpdatePredictionPoints(updatePredictionPointsService)


def getEventDispatcher(
    updatePredictionPoints: Annotated[
        UpdatePredictionPoints, getUpdatePredictionPoints
    ],
):
    event_dispatcher = SimpleEventDispatcher()
    registerEventSubscribers(event_dispatcher, updatePredictionPoints)
    return event_dispatcher
