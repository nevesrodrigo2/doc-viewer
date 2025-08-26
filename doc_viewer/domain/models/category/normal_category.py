from .category import Category
from doc_viewer.domain.models.document.document import Document

class NormalCategory(Category):
    def __init__(self, name: str):
        super().__init__(name)

    
    
