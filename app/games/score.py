from pydantic import BaseModel


class Score(BaseModel):
    homeSideScore: int
    awaySideScore: int
