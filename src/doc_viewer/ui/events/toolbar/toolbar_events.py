# Project Imports
from doc_viewer.domain.events.event import Event

class ToolBarEvent(Event):
    """
    Base class for all ToolBar events.
    """
    pass

class ToolBarToggleFavouriteEvent(ToolBarEvent):
    """
    Event to toggle the favourite status of a document.
    """
    def __init__(self):
        super().__init__()

class ToolBarDeleteDocumentEvent(ToolBarEvent):
    """
    Event to delete a document.
    """
    def __init__(self):
        super().__init__()