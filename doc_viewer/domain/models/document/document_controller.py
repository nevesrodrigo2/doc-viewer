import logging

from .document_factory import DocumentFactory
from .document import Document

from doc_viewer.domain.events.event_bus import event_bus
from doc_viewer.domain.events.document.document_events import(
    DocumentFavouritedEvent,
    DocumentAddedEvent,
    DocumentRemovedEvent
)

logger = logging.getLogger(__name__)  

class DocumentController:
    """Controller for managing document-related operations."""
    def __init__(self):
        self._documents = {}

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
            event_bus.emit(DocumentAddedEvent(document))
            return True
        logger.warning(f"Failed to add document: {file_path}")
        return False

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
            event_bus.emit(DocumentRemovedEvent(document))
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

    def set_favourite(self, file_path: str, is_favourited: bool) -> bool:
        """
        Set the favourite status of a document.

        Args:
            file_path (str): The path of the document to update.
            is_favourited (bool): The new favourite status.

        Returns:
            bool: True if the favourite status was updated, False otherwise.
        """
        if file_path in self._documents:
            self._documents[file_path].set_favourite(is_favourited)
            logger.debug(f"Document {self._documents[file_path].get_title()} "
                         f"favourite status set to {is_favourited}.")
            logger.debug("Emitting DocumentFavouritedEvent...")
            event_bus.emit(
                DocumentFavouritedEvent(self._documents[file_path])
            )
            return True
        logger.error(f"Document not found: {file_path}")
        return False