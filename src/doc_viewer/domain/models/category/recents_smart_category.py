from typing import Callable
from doc_viewer.domain.models.document.document import Document
from doc_viewer.domain.models.category.smart_category import SmartCategory


class RecentsSmartCategory(SmartCategory):

    def __init__(self, name: str):
        super().__init__(name, predicate=lambda doc: True)

    def add_document(self, document: Document) -> bool:
        """
        Adds a document to the recents category if it is not already present.
        The document list is then sorted by last interacted time in descending order.
        Args:
            document (Document): The document to add.
        Returns:
            bool: True if the document was added, False if it was already present.
        """

        added = super().add_document(document)
        if added:
            self.sort_documents()
        return added
        
    
    def sort_documents(self):
        """
        Reorders the documents dict in place by last interacted time (descending).
        """
        documents = self.get_documents()
        sorted_items = sorted(
            documents.items(),
            key=lambda item: item[1].get_last_interacted_at(),
            reverse=True
        )
        # clear and repopulate in the new order
        documents.clear()
        documents.update(sorted_items)