# PySide6 Imports
from PySide6.QtWidgets import (
    QWidget, 
    QVBoxLayout,
)
# Project Imports
from doc_viewer.ui.components.document_viewer.document_catalog import document_catalog
from doc_viewer.ui.components.document_viewer.document_viewer import DocumentViewer
from doc_viewer.ui.components.document_viewer.document.document import UIDocument
from doc_viewer.ui.components.tool_bar import ToolBar
from doc_viewer.domain.events.event_bus import event_bus
from doc_viewer.ui.events.document.ui_document_events import (
    UIDocumentFavouritedEvent,
    UIDocumentRemovedEvent
)
from doc_viewer.ui.events.toolbar.toolbar_events import (
    ToolBarToggleFavouriteEvent,
    ToolBarDeleteDocumentEvent
)
import logging
logger = logging.getLogger(__name__)

class DocumentPanel(QWidget):
    """
    Panel to display the document viewer and tool bar.
    """
    def __init__(self):
        super().__init__()
        self.current_document_path = None

        # layout
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # tool bar
        self.tool_bar = ToolBar()
        self.layout.addWidget(self.tool_bar)
        # document viewer
        self.doc_viewer = DocumentViewer()
        self.layout.addWidget(self.doc_viewer)

        self.subscribe_events()

    def emit_event(self, event):
        """
        Emit an event to the event bus.

        Args:
            event (Event): The event to emit.
        """
        event_bus.emit(event)

    def subscribe_events(self):
        """Subscribe to necessary events."""
        event_bus.subscribe(ToolBarToggleFavouriteEvent, self.handle_events)
        event_bus.subscribe(ToolBarDeleteDocumentEvent, self.handle_events)

    def handle_events(self, event):
        """
        Handle incoming events.
        """
        logger.debug(f"Handling event in DocumentPanel: {event}")
        if isinstance(event, ToolBarToggleFavouriteEvent):
            if self.current_document_path:
                document_path = self.current_document_path
                logger.debug(f"Toggled favourite status for document: {document_path}")
                self.emit_event(UIDocumentFavouritedEvent(document_path))
        elif isinstance(event, ToolBarDeleteDocumentEvent):
            if self.current_document_path:
                document_path = self.current_document_path
                logger.debug(f"Delete requested for document: {document_path}")
                self.emit_event(UIDocumentRemovedEvent(document_path))

    def set_document(self, document_path: str):
        """
        Sets the current document to be displayed in the document panel.

        Args:
            document_path (str): The document to display.
        """
        self.doc_viewer.set_document(document_path)
        self.current_document_path = document_path
        ui_document = document_catalog.get_document(document_path)
        if ui_document:
            is_favourited = ui_document.is_favourited()
            self.tool_bar.update_toolbar_state(
                is_favourited=is_favourited
            )

    def remove_document_catalog(self, document_path: str):
        """
        Remove a document from the catalog.

        Args:
            document_path (str): The document to remove.
        """
        document_catalog.remove_document(document_path)
        