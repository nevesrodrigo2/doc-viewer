# PySide6 Imports
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt

# Project Imports
from doc_viewer.ui.events.document.ui_document_events import (
    UIDocumentThumbnailClickedEvent
)
from doc_viewer.domain.events.event_bus import event_bus   

class Thumbnail(QLabel):
    """
    A widget to display a thumbnail image for a PDF document.
    """

    def __init__(self, document_path: str, pixmap, parent=None):
        super().__init__(parent)
        self.setPixmap(pixmap)
        self.setAlignment(Qt.AlignCenter)
        self.setFixedSize(150, 200)  # Fixed size for thumbnails
        self.setStyleSheet("border: 1px solid black; margin: 5px;")
        self.document_path = document_path

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.on_double_click()
        super().mouseDoubleClickEvent(event)

    def emit_event(self, event):
        """
        Emit an event to the event busit.

        Args:
            event (UIEvent): The event to emit.
        """
        event_bus.emit(event)

    def on_double_click(self):
        """
        Emit your custom UIDocumentThumbnailClickedEvent.
        """
        if self.document_path:
            event = UIDocumentThumbnailClickedEvent(self.document_path)
            self.emit_event(event)