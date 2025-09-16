from typing import Callable, Dict, List, Any, Type
from .event import Event

class EventBus:
    def __init__(self):
        self._subscribers: Dict[Type[Event], List[Callable[[Event], None]]] = {}

    def subscribe(self, event_type: Type[Event], callback: Callable[[Event], None]) -> None:
        """Register a callback for a specific event class."""
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(callback)

    def unsubscribe(self, event_type: Type[Event], callback: Callable[[Event], None]) -> None:
        """Remove a callback for a specific event class."""
        if event_type in self._subscribers:
            self._subscribers[event_type] = [
                cb for cb in self._subscribers[event_type] if cb != callback
            ]

    def emit(self, event: Event) -> None:
        """Trigger an event instance and notify all subscribers."""
        event_type = type(event)
        for child_class in event_type.__mro__:
            if child_class in self._subscribers:
                for callback in self._subscribers[child_class]:
                    callback(event)


event_bus = EventBus()