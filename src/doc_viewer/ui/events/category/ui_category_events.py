from doc_viewer.domain.events.event import Event

class UICategoryEvent(Event):
    """Base class for UI category events."""
    def __init__(self, category):
        self._category = category
    
    def get_category(self):
        """Returns the category associated with the event."""
        return self._category
    
class UICategoryThumbnailPanelEvent(UICategoryEvent):
    """Event for when the thumbnail panel is updated."""
    def __init__(self, category, thumbnail_panel):
        super().__init__(category)
        self._thumbnail_panel = thumbnail_panel
    
    def get_thumbnail_panel(self):
        """Returns the thumbnail panel associated with the event."""
        return self._thumbnail_panel