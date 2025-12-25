from pydantic import BaseModel
from sqlmodel import Field, SQLModel


class Prediction(BaseModel):
    predictionId: int
    gameId: int
    homeSideScore: int
    awaySideScore: int


class DbPrediction(SQLModel):
    predictionId: int | None = Field(default=None, primary_key=True)
    gameId: int
    homeSideScore: int
    awaySideScore: int
