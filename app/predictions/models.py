from pydantic import BaseModel
from sqlmodel import Field, SQLModel


class Prediction(BaseModel):
    predictionId: int
    gameId: int
    homeSideScore: int
    awaySideScore: int
    points: int = Field(default=0)

    def updatePoints(self, points):
        self.points = points


class DbPrediction(SQLModel, table=True):
    predictionId: int | None = Field(default=None, primary_key=True)
    gameId: int
    homeSideScore: int
    awaySideScore: int
    points: int
