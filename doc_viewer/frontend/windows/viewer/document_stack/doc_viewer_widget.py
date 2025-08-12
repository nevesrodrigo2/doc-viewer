from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtPdf import QPdfDocument

class DocumentViewer(QPdfView):
    """ A widget for viewing PDF documents using QPdfView."""
    def __init__(self, document_path: str, parent=None):
        super().__init__()
        self.document_path = document_path
        self.doc = QPdfDocument(self)
        self.doc.load(self.document_path)

        # page mode
        self.setPageMode(QPdfView.PageMode.MultiPage)

        self.setDocument(self.doc)
        self.setZoomMode(QPdfView.ZoomMode.FitInView)