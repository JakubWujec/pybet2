from functools import cache, partial
from typing import Annotated

from fastapi import Depends

from app.games.repository import InMemoryGameRepository
from app.predictions.repository import InMemoryPredictionRepository
from app.predictions.service import MakePredictionService


gameRepository = InMemoryGameRepository()
predictionRepository = InMemoryPredictionRepository()


def get_game_repository():
    return gameRepository


@cache
def get_prediction_repository():
    return predictionRepository


def getMakePredictionService():
    return MakePredictionService(get_game_repository(), get_prediction_repository())
