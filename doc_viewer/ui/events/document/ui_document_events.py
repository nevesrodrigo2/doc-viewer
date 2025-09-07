# Project Imports
from doc_viewer.ui.events.ui_event import UIEvent

class UIDocumentEvent(UIEvent):
    """
    Base class for all document-related UI events.
    """
    def __init__(self, document_path: str):
        self._document_path = document_path

    def get_document_path(self) -> str:
        return self._document_path
    
class UIDocumentOpenedEvent(UIDocumentEvent):
    """
    Event emitted when a document is opened in the UI.
    """
    def __init__(self, document_path: str):
        super().__init__(document_path)

class UIDocumentAddedEvent(UIDocumentEvent):
    """
    Event emitted when a document is added to the UI.
    """
    def __init__(self, document_path: str):
        super().__init__(document_path)

class UIDocumentClosedEvent(UIDocumentEvent):
    """
    Event emitted when a document is closed in the UI.
    """
    def __init__(self, document_path: str):
        super().__init__(document_path)

class UIDocumentRemovedEvent(UIDocumentEvent):
    """
    Event emitted when a document is removed from the UI.
    """
    def __init__(self, document_path: str):
        super().__init__(document_path)

class UIDocumentThumbnailClickedEvent(UIDocumentEvent):
    """
    Event emitted when a document thumbnail is clicked in the UI.
    """
    def __init__(self, document_path: str):
        super().__init__(document_path)