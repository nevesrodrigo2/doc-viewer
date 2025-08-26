import logging

from .category import Category
from  typing import Callable

from doc_viewer.domain.models.document.document import Document

logger = logging.getLogger(__name__)  

class SmartCategory(Category):
    def __init__(self, name: str, predicate: Callable[[Document], bool]):
        super().__init__(name)
        self._predicate = predicate

    def add_document(self, document: Document) -> bool:
        """
        Adds a document to the category if it meets the criteria defined by the predicate.

        Args:
            document (Document): The document to add.

        Returns:
            bool: True if the document was added, False otherwise.
        """
        logger.debug("Checking predicate...")
        if self._predicate(document):
            logger.debug("Predicate passed.")
            return super().add_document(document)
        logger.debug("Predicate failed.")
        return False