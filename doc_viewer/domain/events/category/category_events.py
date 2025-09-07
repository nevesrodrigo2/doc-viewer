# Project Imports
from doc_viewer.domain.events.event import Event

class CategoryEvent(Event):
    """
    Base class for category events.
    """
    def __init__(self, category_name: str):
        self._category_name = category_name

    def get_category_name(self) -> str:
        return self._category_name

class DocumentAddedCategoryEvent(CategoryEvent) :
    """
    Event emitted when a document is added to a 
    category.
    """
    def __init__(self, category_name: str, document_file_path: str):
        super().__init__(category_name)
        self._document_file_path = document_file_path

    def get_document_file_path(self) -> str:
        return self._document_file_path
