class EventBus:
    def __init__(self):
        self._subscribers = {}

    def subscribe(self, event_name, callback):
        if event_name not in self._subscribers:
            self._subscribers[event_name] = []
        self._subscribers[event_name].append(callback)

    def emit(self, event_name, *args, **kwargs):
        for callback in self._subscribers.get(event_name, []):
            callback(*args, **kwargs)

# setting up the event bus
event_bus = EventBus()