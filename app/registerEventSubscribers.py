from functools import partial
from app.eventDispatcher import EventDispatcher
from app.games.events import GameScoreFilled
from app.predictions.service import UpdatePredictionPoints


def registerEventSubscribers(
    eventDispatcher: EventDispatcher, updatePredictionPoints: UpdatePredictionPoints
):
    eventDispatcher.subscribeToEvent(
        GameScoreFilled,
        partial(
            updatePredictionPoints.whenGameScoreUpdated,
        ),
    )
