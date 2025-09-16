from collections import deque


from doc_viewer.domain.models.document.document import Document

def is_favourited(doc: Document) -> bool:
    return doc.is_favourited()  