from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtPdf import QPdfDocument
from PySide6.QtCore import Qt

from doc_viewer.frontend.events.event_bus import event_bus

class DocumentViewer(QPdfView):
    """ A widget for viewing PDF documents using QPdfView."""
    def __init__(self, document_path: str, parent=None):
        super().__init__()
        self.document_path = document_path
        self.doc = QPdfDocument(self)
        self.doc.load(self.document_path)

        # page mode
        self.setPageMode(QPdfView.PageMode.MultiPage)
        # zoom settings
        self.setZoomMode(QPdfView.ZoomMode.Custom)
        # self.setZoomMode(QPdfView.ZoomMode.FitInView)
        self.setZoomFactor(1.0)
        # set doc
        self.setDocument(self.doc)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # set event handler
        event_bus.subscribe('zoom_level_changed', self.set_zoom_factor)

    def set_zoom_factor(self, zoom_factor: float):
        """Set the zoom factor for the document viewer."""

        if isinstance(zoom_factor, int):
            zoom_factor = zoom_factor / 100.0

        if zoom_factor <= 0:
            raise ValueError("Zoom factor must be greater than 0")
        self.setZoomFactor(zoom_factor)

    def decrement_zoom(self):
        """Decrease the zoom level"""
        current_zoom = self.zoomFactor()
        new_zoom = max(0.1, current_zoom - 0.5)
        self.setZoomFactor(new_zoom)

    def increment_zoom(self):
        """Increase the zoom level"""
        current_zoom = self.zoomFactor()
        new_zoom = current_zoom + 0.5
        self.setZoomFactor(new_zoom)