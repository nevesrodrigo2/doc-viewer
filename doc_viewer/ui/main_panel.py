# PySide6 Imports
from PySide6.QtWidgets import (
    QWidget, 
    QStackedLayout
)

# Project Imports
from doc_viewer.ui.components.document_viewer.document_viewer import DocumentViewer
from doc_viewer.ui.components.document_viewer.thumbnail_panel import ThumbnailPanel
from doc_viewer.domain.events.event_bus import event_bus
from doc_viewer.ui.events.category.ui_library_events import (
    UILibraryThumbnailPanelEvent
)
from doc_viewer.ui.events.category.ui_category_events import (
    UICategoryThumbnailPanelEvent
)
from doc_viewer.ui.events.document.ui_document_events import (
    UIDocumentThumbnailClickedEvent
)

import logging
logger = logging.getLogger(__name__)

class MainPanel(QWidget):
    """Main panel containing the document viewer stack."""
    def __init__(self):
        super().__init__()
        self.layout = QStackedLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.setup_document_viewer()
        self.setup_thumbnail_panel()
        self.subscribe_events()

    def setup_document_viewer(self):
        """Setup the document viewer."""
        self.doc_viewer = DocumentViewer()
        self.layout.addWidget(self.doc_viewer)
        self.layout.setCurrentIndex(0)

    def setup_thumbnail_panel(self):
        """Setup the thumbnail panel."""

        self.thumbnail_panel = ThumbnailPanel()
        self.layout.addWidget(self.thumbnail_panel)
        self.layout.setCurrentIndex(1)

    def subscribe_events(self):
        """Subscribe to necessary events."""
        event_bus.subscribe(UILibraryThumbnailPanelEvent, self.handle_events) 
        event_bus.subscribe(UICategoryThumbnailPanelEvent, self.handle_events)
        event_bus.subscribe(UIDocumentThumbnailClickedEvent, self.handle_events)

    def handle_events(self, event):
        """
        Handle incoming UI events.
        
        Args:
            event (UILibraryEvent): The event to handle.
        """
        logger.debug(f"Handling {event}...")
        if isinstance(event, (
            UILibraryThumbnailPanelEvent, 
            UICategoryThumbnailPanelEvent
        )):
            thumbnail_panel = event.get_thumbnail_panel()
            print(thumbnail_panel)
            if thumbnail_panel:
                self.set_thumbnail_panel(thumbnail_panel)
                # self.set_current_viewer(1)
        elif isinstance(event, UIDocumentThumbnailClickedEvent):
            document_path = event.get_document_path()
            self.set_document(document_path)
            self.set_current_viewer(0)

    def get_document_viewer(self) -> DocumentViewer:
        """Returns the document viewer instance."""
        return self.doc_viewer
    
    def set_current_viewer(self, index: int):
        """
        Sets the current viewer by index.

        Args:
            index (int): The index of the viewer to display.
        """
        self.layout.setCurrentIndex(index)

    def set_document(self, document):
        """
        Sets the current document to be displayed in the document viewer.

        Args:
            document: The document to display.
        """
        self.doc_viewer.set_document(document)

    def set_thumbnail_panel(self, panel):
        """
        Sets the thumbnail panel as the current viewer.

        Args:
            panel: The thumbnail panel to display.
        """
        if panel == self.thumbnail_panel:
            logger.debug("Same panel, just setting current widget")
            self.layout.setCurrentWidget(self.thumbnail_panel)
            return
            
        logger.debug("Different panel, replacing...")
        self.layout.removeWidget(self.thumbnail_panel)
        self.thumbnail_panel = panel
        self.layout.addWidget(self.thumbnail_panel)
        self.layout.setCurrentWidget(self.thumbnail_panel)
