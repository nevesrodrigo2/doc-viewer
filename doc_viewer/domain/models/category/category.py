import logging
from doc_viewer.domain.models.document.document import Document
from doc_viewer.domain.events.event_bus import event_bus
from doc_viewer.domain.events.category.category_events import (
    DocumentAddedCategoryEvent
)

logger = logging.getLogger(__name__)  

class Category:
    def __init__(self, name: str):
        self._name = name
        self._documents = {}

    def emit_event(self, event):
        """
        Emit an event to the event bus.

        Args:
            event: The event to emit.
        """
        event_bus.emit(event)

    def get_name(self) -> str:
        """Returns the name of the category."""
        return self._name

    def get_documents(self) -> dict[str, Document]:
        """Returns the list of documents in the category."""
        return self._documents

    def add_document(self, document: Document) -> bool:
        """
        Adds a document to the category.

        Args:
            document (Document): The document to add.

        Returns:
            bool: True if the document was added, False if it was already present.
        """
        logger.debug(f"Adding document '{document.get_title()}' to category '{self._name}'")
        documents = self.get_documents()
        if document.get_file_path() not in documents.keys():
            self._documents[document.get_file_path()] = document
            logger.debug(f"Document '{document.get_title()}' added to category '{self._name}'")
            # emit event, document added to category
            # propagate to UI
            self.emit_event(DocumentAddedCategoryEvent(self.get_name(), document.get_file_path()))
            return True
        logger.debug(f"Document '{document.get_title()}' already present in category '{self._name}'")
        return False

    def remove_document(self, document: Document) -> bool:
        """
        Removes a document from the category.

        Args:
            document (Document): The document to remove.

        Returns:
            bool: True if the document was removed, False if it was not found.
        """
        logger.debug(f"Removing document '{document.get_title()}' from category '{self._name}'")
        documents = self.get_documents()
        if document.get_file_path() in documents.keys():
            del self._documents[document.get_file_path()]
            logger.debug(f"Document '{document.get_title()}' removed from category '{self._name}'")
            return True
        logger.debug(f"Document '{document.get_title()}' not found in category '{self._name}'")
        return False
    
    def clear_documents(self) -> None:
        """
        Clears all documents from the category.
        """
        logger.debug(f"Clearing all documents from category '{self._name}'")
        self._documents.clear()

    def get_document_count(self) -> int:
        """
        Returns the number of documents in the category.
        """
        return len(self._documents)