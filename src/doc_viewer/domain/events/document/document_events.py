
from doc_viewer.domain.events.event import Event
from doc_viewer.domain.models.document.document import Document

class DocumentEvent(Event):
    """Base class for document events."""
    def __init__(self, document: Document):
        self._document = document

    def get_document(self) -> Document:
        return self._document
    
class DocumentFavouritedEvent(DocumentEvent):
    """Event emitted when a document is favourited."""
    def __init__(self, document: Document):
        super().__init__(document)

class DocumentAddedEvent(DocumentEvent):
    """Event emitted when a document is added."""
    def __init__(self, document: Document):
        super().__init__(document)  
    
class DocumentRemovedEvent(DocumentEvent):
    """Event emitted when a document is removed."""
    def __init__(self, document: Document):
        super().__init__(document)

    
