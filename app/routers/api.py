from fastapi import APIRouter
from app.routers.games import router as games_router
from app.routers.predictions import router as predictions_router

router = APIRouter()

router.include_router(games_router)
router.include_router(predictions_router)
