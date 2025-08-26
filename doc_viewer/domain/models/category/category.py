import logging
from doc_viewer.domain.models.document.document import Document

logger = logging.getLogger(__name__)  

class Category:
    def __init__(self, name: str):
        self._name = name
        self._documents = []

    def get_name(self) -> str:
        """Returns the name of the category."""
        return self._name

    def get_documents(self) -> list:
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
        if document not in self._documents:
            self._documents.append(document)
            logger.debug(f"Document '{document.get_title()}' added to category '{self._name}'")
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
        if document in self._documents:
            self._documents.remove(document)
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