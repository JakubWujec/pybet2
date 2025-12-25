from typing import Callable, Dict, List, Protocol, Type
from app import events


class EventDispatcher(Protocol):
    def dispatchAll(self, events: list[events.BaseEvent]): ...
    def subscribeToEvent(self, event: type[events.BaseEvent], subscriber): ...


class SimpleEventDispatcher:
    def __init__(self) -> None:
        self.subscribersForEvent: Dict[Type[events.BaseEvent], List[Callable]] = {}

    def subscribeToEvent(self, event: type[events.BaseEvent], subscriber):
        if event not in self.subscribersForEvent:
            self.subscribersForEvent[event] = []
        self.subscribersForEvent[event].append(subscriber)

    def dispatchAll(self, events: list[events.BaseEvent]):
        for event in events:
            self.dispatch(event)

    def dispatch(self, event: events.BaseEvent):
        subscribers = self.subscribersForEvent[type(event)]
        for subscriber in subscribers:
            subscriber(event)
