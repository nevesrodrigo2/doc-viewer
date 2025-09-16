# Project Imports
from doc_viewer.domain.events.event import Event

class UILibraryEvent(Event):
    """Event related to the UI library."""
    def __init__(self, library):
        self._library = library
    
    def get_library(self):
        """Returns the library associated with the event."""
        return self._library
    
class UILibraryThumbnailPanelEvent(UILibraryEvent):
    """Event for when the thumbnail panel is updated."""
    def __init__(self, library, thumbnail_panel):
        super().__init__(library)
        self._thumbnail_panel = thumbnail_panel
    
    def get_thumbnail_panel(self):
        """Returns the thumbnail panel associated with the event."""
        return self._thumbnail_panel