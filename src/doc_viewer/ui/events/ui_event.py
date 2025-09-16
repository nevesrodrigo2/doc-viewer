# Project Imports
from doc_viewer.domain.events.event import Event

class UIEvent(Event):
    """Base class for all UI events."""
    def __init__(self):
        super().__init__()