from typing import Callable
from doc_viewer.domain.models.document.document import Document
from doc_viewer.domain.models.category.smart_category import SmartCategory


class RecentsSmartCategory(SmartCategory):

    def __init__(self, name: str):
        super().__init__(name, predicate=lambda doc: True)

    def add_document(self, document: Document) -> bool:
        """"""
        if document not in self.get_documents():
            self.get_documents().insert(0, document)
            return True
        return False
    
    def sort_documents(self):
        documents = self.get_documents()
        documents.sort(key=lambda doc: doc.get_last_interacted_at(), reverse=False)