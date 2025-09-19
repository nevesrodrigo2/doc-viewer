# Project Imports
from doc_viewer.ui.components.document_viewer.document.document import UIDocument

class DocumentCatalog:
    """
    A catalog to manage documents.
    """
    def __init__(self):
        self.documents = {}

    def add_document(self, file_path: str, document):
        """
        Add a document to the catalog.

        Args:
            file_path (str): The path of the document.
            document: The document object.
        """
        self.documents[file_path] = document

    def get_document(self, file_path: str) -> UIDocument:
        """
        Get a document from the catalog.

        Args:
            file_path (str): The path of the document.

        Returns:
            The document (UIDocument) object if found, else None.
        """
        return self.documents.get(file_path, None)

    def remove_document(self, file_path: str):
        """
        Remove a document from the catalog.

        Args:
            file_path (str): The path of the document.
        """
        if file_path in self.documents:
            del self.documents[file_path]

    def get_documents(self) -> dict[str, UIDocument]:
        """
        Get all documents from the catalog.

        Returns:
            dict: A dictionary of all documents in the catalog.
        """
        return self.documents
    
    def get_document_count(self) -> int:
        """
        Get the count of documents in the catalog.

        Returns:
            int: The number of documents in the catalog.
        """
        return len(self.documents)

document_catalog = DocumentCatalog()