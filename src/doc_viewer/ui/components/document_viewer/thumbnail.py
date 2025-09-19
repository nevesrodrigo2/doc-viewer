# PySide6 Imports
from PySide6.QtWidgets import QLabel, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

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
        self.setObjectName("thumbnail")
        self.setPixmap(pixmap)
        self.setAlignment(Qt.AlignCenter)
        self.setFixedSize(150, 200)  
        self.setMouseTracking(True)  # Needed for hover
        self.setAutoFillBackground(True)

        self._document_path = document_path

        self.shadow = QGraphicsDropShadowEffect(blurRadius=15, xOffset=0, yOffset=0)
        self.shadow.setColor(QColor(255, 255, 255, 200))  # white glow
        self.shadow.setEnabled(False)
        self.setGraphicsEffect(self.shadow)

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
        document_path = self.get_document_path()
        if document_path:
            event = UIDocumentThumbnailClickedEvent(document_path)
            self.emit_event(event)

    def get_document_path(self) -> str:
        """
        Get the document path associated with this thumbnail.

        Returns:
            str: The document path.
        """
        return self._document_path