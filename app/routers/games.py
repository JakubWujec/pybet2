from typing import Annotated
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.dependencies import get_game_repository
from app.games.models import Game
from app.games.repository import GameRepository

router = APIRouter(
    prefix="/games",
)


class CreateGame(BaseModel):
    home_side: str
    away_side: str
    kickoff: str

    def to_model(self, gameId: int) -> Game:
        return Game(
            gameId=gameId,
            home_side=self.home_side,
            away_side=self.away_side,
            kickoff=self.kickoff,
        )


@router.post("/")
async def createGame(
    createGame: CreateGame,
    gameRepository: Annotated[GameRepository, Depends(get_game_repository)],
):
    nextId = gameRepository.getNextId()
    gameRepository.save(createGame.to_model(nextId))

    return {"gameId": nextId}


@router.get("/{id}/")
async def getById(id: int):
    return {
        "game": {
            "gameId": id,
            "home_side": "Arsenal",
            "away_side": "Spurs",
            "kickoff": "2027-12-24 11:30",
        }
    }
