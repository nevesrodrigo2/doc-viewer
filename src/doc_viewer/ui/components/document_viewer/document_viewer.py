# PySide6 Imports
from PySide6.QtPdfWidgets import QPdfView

# Project Imports
from doc_viewer.ui.components.document_viewer.document.pdf_document import PDFDocument
from doc_viewer.ui.components.document_viewer.document_catalog import document_catalog

class DocumentViewer(QPdfView):
    """
    A stacked layout to manage multiple document viewers.
    """
    def __init__(self):
        super().__init__()

    def set_document(self, document_path:str):
        """
        Sets the current document to be displayed.

        Args:
            document (str): The path to the PDF document.
        """
        document = document_catalog.get_document(document_path)
        if document:
            self.setDocument(document)