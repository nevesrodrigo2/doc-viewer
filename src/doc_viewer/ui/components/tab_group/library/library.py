# PySide6 Imports
from PySide6.QtWidgets import (
    QTreeWidgetItem
)

# Project Imports
from doc_viewer.ui.components.document_viewer.document.document import UIDocument
from doc_viewer.ui.components.document_viewer.document.document_factory import DocumentFactory
from doc_viewer.ui.components.document_viewer.thumbnail_panel import ThumbnailPanel
from doc_viewer.domain.events.event_bus import event_bus
from doc_viewer.ui.events.document.ui_document_events import (
    UIDocumentOpenedEvent,
    UIDocumentEvent,
    UIDocumentAddedEvent,
)
from doc_viewer.ui.events.category.ui_library_events import UILibraryEvent, UILibraryThumbnailPanelEvent    
from doc_viewer.ui.components.document_viewer.document_catalog import document_catalog
import logging

logger = logging.getLogger(__name__)

class Library(QTreeWidgetItem):
    """
    A tree widget item that represents a library of documents.
    """
    def __init__(self):
        super().__init__(["Library"])
        self._documents = {}
        self._thumbnail_panel = ThumbnailPanel()
        self.subscribe_events()

    def emit_event(self, event):
        """
        Emit an event to the event busit.

        Args:
            event (UIDocumentEvent): The event to emit.
        """
        event_bus.emit(event)

    def subscribe_events(self):
        """Subscribe to relevant UI events."""
        event_bus.subscribe(UIDocumentOpenedEvent, self.handle_events)

    def handle_events(self, event):
        """
        Handle incoming UI events.
        
        Args:
            event (UIDocumentEvent): The event to handle.
        """
        logger.debug(f"Handling event: {event}")
        if isinstance(event, UIDocumentOpenedEvent):
            document_path = event.get_document_path()
            if self.add_document(document_path):
                self.emit_event(UIDocumentAddedEvent(document_path))
            else:
                logger.error(f"Document already in library: {document_path}")

    def add_document(self, document_path: str) -> bool:
        """
        Add a document to the library.
        Args:
            document (UIDocument): The document to add.

        Returns:
            bool: True if the document was added, False if it was already
            present.
        """
        if document_path not in self._documents.keys():
            document = DocumentFactory.create_document(document_path)
            self._documents[document_path] = document
            self._thumbnail_panel.add_thumbnail_viewer(document)
            document_catalog.add_document(document_path, document)
            return True
        return False

    def get_documents(self) -> dict[str, UIDocument]:
        """
        Get the list of documents in the library.

        Returns:
            dict[str, UIDocument]: The list of documents.
        """
        return self._documents
    
    def get_thumbnail_panel(self) -> ThumbnailPanel:
        """
        Get the thumbnail panel associated with the library.

        Returns:
            ThumbnailPanel: The thumbnail panel.
        """
        return self._thumbnail_panel
    
    def on_double_click(self):
        """
        Handle double-click event on the library item.
        Emits an event to notify other components.
        """
        logger.debug("Library item double-clicked.")
        self.emit_event(UILibraryThumbnailPanelEvent(
            self, 
            self._thumbnail_panel
            )
        )