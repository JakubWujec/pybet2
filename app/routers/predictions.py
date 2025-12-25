from typing import Annotated
from fastapi import APIRouter, Depends

from app.dependencies import getMakePredictionService
from app.predictions.service import MakePrediction, MakePredictionService


router = APIRouter(
    prefix="/predictions",
)


@router.post("/")
async def makePrediction(
    makePrediction: MakePrediction,
    makePredictionService: Annotated[
        MakePredictionService, Depends(getMakePredictionService)
    ],
):
    predictionId = makePredictionService.make(makePrediction)
    return {"predictionId": predictionId}
