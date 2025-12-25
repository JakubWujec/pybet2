from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from app.db_session import get_session
from app.games.repository import (
    GameRepository,
    SqlGameRepository,
)
from app.predictions.repository import (
    InMemoryPredictionRepository,
    PredictionRepository,
    SqlPredictionRepository,
)
from app.predictions.service import MakePredictionService


predictionRepository = InMemoryPredictionRepository()


def get_game_repository(session: Annotated[Session, Depends(get_session)]):
    return SqlGameRepository(session)


def get_prediction_repository(session: Annotated[Session, Depends(get_session)]):
    return SqlPredictionRepository(session)


def getMakePredictionService(
    gameRepository: Annotated[GameRepository, Depends(get_game_repository)],
    predictionRepository: Annotated[
        PredictionRepository, Depends(get_prediction_repository)
    ],
):
    return MakePredictionService(gameRepository, predictionRepository)
