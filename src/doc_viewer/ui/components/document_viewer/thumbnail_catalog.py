# PySide6 Imports 
from PySide6.QtGui import QPixmap, QImage

# Project Imports
from doc_viewer.domain.events.event_bus import event_bus
from doc_viewer.ui.events.document.ui_document_events import (
    UIDocumentThumbnailClickedEvent
)

class ThumbnailCatalog:
    """
    Catalog to manage and store thumbnails for documents.
    This catalog does not handle thumbnail widgets, but instead 
    saves the QPixmap objects associated with document paths.
    """
    def __init__(self):
        self.thumbnails = {}

    def emit_event(self, event):
        """
        Emit an event to the event busit.

        Args:
            event (UIEvent): The event to emit.
        """
        event_bus.emit(event)

    def add_thumbnail(self, document_path: str, thumbnail: QPixmap):
        """
        Add a thumbnail to the catalog.
        Args:
            document_path (str): The path of the document.
            thumbnail (QPixmap): The thumbnail pixmap.
        """
        self.thumbnails[document_path] = thumbnail

    def get_thumbnail(self, document_path: str) -> QPixmap:
        """
        Get a thumbnail from the catalog.
        Args:
            document_path (str): The path of the document.

        Returns:
            QPixmap: The thumbnail pixmap, or None if not found.
        """
        return self.thumbnails.get(document_path)

    def remove_thumbnail(self, document_path: str):
        """
        Remove a thumbnail from the catalog.
        Args:
            document_path (str): The path of the document.
        """
        if document_path in self.thumbnails:
            del self.thumbnails[document_path]

    def get_thumbnails(self) -> dict[str, QPixmap]:
        """
        Get all thumbnails from the catalog.

        Returns:
            dict[str, QPixmap]: A dictionary of document paths and their associated thumbnails.
        """
        return self.thumbnails

thumbnail_catalog = ThumbnailCatalog()