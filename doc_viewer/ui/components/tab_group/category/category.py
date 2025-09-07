# PySide6 Imports
from PySide6.QtWidgets import (
    QTreeWidgetItem
)

# Project Imports
from doc_viewer.domain.models.document.document import Document
from doc_viewer.ui.components.document_viewer.thumbnail_panel import ThumbnailPanel
from doc_viewer.ui.events.category.ui_category_events import (
    UICategoryThumbnailPanelEvent
)
from doc_viewer.domain.events.category.category_events import (
    DocumentAddedCategoryEvent
)
from doc_viewer.ui.components.document_viewer.document_catalog import document_catalog
from doc_viewer.domain.events.event_bus import event_bus
import logging
logger = logging.getLogger(__name__)

class Category(QTreeWidgetItem):
    def __init__(self, name: str):
        super().__init__([name])
        self._name = name
        self._documents = {}
        self._thumbnail_panel = ThumbnailPanel()
        self.subscribe_events()

    def emit_event(self, event):
        """
        Emit an event to the event bus.

        Args:
            event (UICategoryThumbnailPanelEvent): The event to emit.
        """
        event_bus.emit(event)

    def subscribe_events(self):
        """Subscribe to relevant UI events."""
        event_bus.subscribe(DocumentAddedCategoryEvent, self.handle_events)

    def handle_events(self, event):
        """
        Handle incoming UI events.
        
        Args:
            event (Event): The event to handle.
        """
        logger.debug(f"Handling event in Category: {event}")
        if isinstance(event, DocumentAddedCategoryEvent):            # Check if this event is for this category
            if event.get_category_name() == self._name:
                self.add_document(event.get_document_file_path())

    def add_document(self, document_path: str) -> bool:
        """
        Add a document to this category.

        Args:
            document_path (str): The path of the document to add.

        Returns:
            bool: True if the document was added, False if it was already present.
        """
        thumbnail_panel = self.get_thumbnail_panel()
        documents = self.get_documents()
        document = document_catalog.get_document(document_path)
        if document and document_path not in documents.keys():
            self._documents[document_path] = document
            thumbnail_panel.add_thumbnail_viewer(document)
            return True
        return False

    def get_documents(self) -> list[Document]:
        """
        Get the list of documents in this category.
        
        Returns:
            list[Document]: The list of documents.
        """
        return self._documents

    def get_name(self) -> str:
        """
        Get the name of the category.

        Returns:
            str: The name of the category.
        """
        return self._name

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
        logger.debug(f"{self.get_name()} item double-clicked.")
        self.emit_event(
            UICategoryThumbnailPanelEvent(
                self, 
                self._thumbnail_panel
            )
        )