from pydantic import BaseModel


class Prediction(BaseModel):
    predictionId: int
    gameId: int
    homeSideScore: int
    awaySideScore: int
