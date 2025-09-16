import datetime
import logging

from .document_factory import DocumentFactory
from .document import Document

from doc_viewer.domain.events.event_bus import event_bus
from doc_viewer.domain.events.document.document_events import(
    DocumentFavouritedEvent,
    DocumentAddedEvent,
    DocumentRemovedEvent
)
from doc_viewer.ui.events.document.ui_document_events import (
    UIDocumentEvent,
    UIDocumentAddedEvent,
    UIDocumentFavouritedEvent,
    UIDocumentRemovedEvent
)

logger = logging.getLogger(__name__)  

class DocumentController:
    """Controller for managing document-related operations."""
    def __init__(self):
        self._documents = {}
        self.subscribe_events()

    def emit_event(self, event):
        """Emit an event to the event bus."""
        event_bus.emit(event)

    def subscribe_events(self):
        """Subscribe to relevant document events."""
        event_bus.subscribe(UIDocumentAddedEvent, self.handle_events)
        event_bus.subscribe(UIDocumentFavouritedEvent, self.handle_events)
        event_bus.subscribe(UIDocumentRemovedEvent, self.handle_events)

    def handle_events(self, event: UIDocumentEvent):
        """
        Handle incoming document events.

        Args:
            event (UIDocumentEvent): The event to handle.
        """
        logger.debug(f"Handling {event}...")
        if isinstance(event, UIDocumentAddedEvent):
            file_path = event.get_document_path()
            self.add_document(file_path)
        elif isinstance(event, UIDocumentFavouritedEvent):
            file_path = event.get_document_path()
            self.set_favourite(file_path)
        elif isinstance(event, UIDocumentRemovedEvent):
            file_path = event.get_document_path()
            self.remove_document(file_path)
              
    def add_document(self, file_path: str) -> bool:
        """
        Add a document to the controller.

        Args:
            file_path (str): The path to the document file.

        Returns:
            bool: True if the document was added successfully, False otherwise.
        """
        document = DocumentFactory.create_document(file_path)
        if document:
            self._documents[file_path] = document
            logger.debug(f"Document added: {file_path}")
            self.emit_event(DocumentAddedEvent(document))
            return True
        logger.warning(f"Failed to add document: {file_path}")
        return False

    def get_document(self, file_path: str) -> Document | None:
        """
        Get a document by file path.

        Args:
            file_path (str): The path of the document to retrieve.

        Returns:
            Document | None: The document if found, None otherwise.
        """
        return self.get_documents().get(file_path)

    def remove_document(self, file_path: str) -> bool:
        """
        Remove a document by file path.

        Args:
            file_path (str): The path of the document to remove.

        Returns:
            bool: True if the document was removed, False otherwise.
        """
        if file_path in self._documents:
            document = self._documents[file_path]
            self.emit_event(DocumentRemovedEvent(document))
            del self._documents[file_path]
            logger.debug(f"Document removed: {file_path}")
            return True
        logger.error(f"Document not found: {file_path}")
        return False

    def get_documents(self) -> list[Document]:
        """
        Get a list of all documents.

        Returns:
            list[Document]: The list of documents.
        """
        return self._documents

    def is_favourited(self, file_path: str) -> bool:
        """
        Check if a document is favourited.

        Args:
            file_path (str): The path of the document to check.

        Returns:
            bool: True if the document is favourited, False otherwise.
        """
        if file_path in self._documents:
            return self._documents[file_path].is_favourited()
        logger.error(f"Document not found: {file_path}")
        return False

    def set_favourite(
            self, 
            file_path: str
    ) -> bool:
        """
        Set the favourite status of a document.

        Args:
            file_path (str): The path of the document to update.

        Returns:
            bool: True if the favourite status was updated, False otherwise.
        """
        if file_path in self._documents:
            doc = self.get_document(file_path)

            # set the favourite status
            # opposite of the current fav status
            doc.set_favourite(not doc.is_favourited())

            logger.debug(
                f"Document {doc.get_title()} "
                f"favourite status set to {doc.is_favourited()}."
            )
            logger.debug("Emitting DocumentFavouritedEvent...")
            self.set_last_interacted_at(file_path)
            self.emit_event(DocumentFavouritedEvent(doc))
            return True
        logger.error(f"Document not found: {file_path}")
        return False

    def set_last_interacted_at(
            self, 
            file_path: str
    ) -> bool:
        """
        Set the last interacted timestamp for a document.

        Args:
            file_path (str): The path of the document to update.
            timestamp (datetime): The timestamp to set.
        """
        if file_path in self._documents:
            self._documents[file_path].set_last_interacted_at(
                datetime.datetime.now()
            )
            logger.debug(f"Document {self._documents[file_path].get_title()} "
                         f"last interacted at set to now.")
            return True
        logger.error(f"Document not found: {file_path}")
        return False