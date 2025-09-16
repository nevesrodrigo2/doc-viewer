# PySide6 Imports
from PySide6.QtWidgets import (
    QWidget, 
    QStackedLayout
)
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt

# Project Imports
from doc_viewer.ui.components.document_panel import DocumentPanel
from doc_viewer.ui.components.document_viewer.thumbnail_panel import ThumbnailPanel
from doc_viewer.domain.events.event_bus import event_bus
from doc_viewer.ui.events.category.ui_library_events import (
    UILibraryThumbnailPanelEvent
)
from doc_viewer.ui.events.category.ui_category_events import (
    UICategoryThumbnailPanelEvent
)
from doc_viewer.ui.events.document.ui_document_events import (
    UIDocumentThumbnailClickedEvent,
    UIDocumentRemovedEvent
)

import logging
logger = logging.getLogger(__name__)

class MainPanel(QWidget):
    """Main panel containing the document viewer stack."""
    def __init__(self):
        super().__init__()
        # set keyboard focus
        self.setFocusPolicy(Qt.StrongFocus)
        # setup layout
        self.layout = QStackedLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # setup methods
        self.setup_document_panel()
        self.setup_thumbnail_panel()
        self.subscribe_events()

    def keyPressEvent(self, event: QKeyEvent):
        """Handle key press events."""
        key_name = Qt.Key(event.key()).name

        # check for escape key to return to thumbnail view
        if event.key() == Qt.Key.Key_Escape:
            if self.layout.currentIndex() != 1:
                logger.debug(f"Key pressed: {key_name}")    
                self.set_current_viewer(1)

    def subscribe_events(self):
        """Subscribe to necessary events."""
        event_bus.subscribe(UILibraryThumbnailPanelEvent, self.handle_events) 
        event_bus.subscribe(UICategoryThumbnailPanelEvent, self.handle_events)
        event_bus.subscribe(UIDocumentThumbnailClickedEvent, self.handle_events)
        event_bus.subscribe(UIDocumentRemovedEvent, self.handle_events)
    
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
            if thumbnail_panel:
                self.set_thumbnail_panel(thumbnail_panel)
                # self.set_current_viewer(1)
        elif isinstance(event, UIDocumentThumbnailClickedEvent):
            document_path = event.get_document_path()
            self.set_document(document_path)
            self.set_current_viewer(0)
        elif isinstance(event, UIDocumentRemovedEvent):
            # After a document is removed, switch back to the thumbnail view
            document_path = event.get_document_path()

            # Remove the thumbnail viewer and its catalog entry
            self.thumbnail_panel.remove_thumbnail_viewer(document_path)
            self.thumbnail_panel.remove_thumbnail(document_path)
            # Remove the document from the document catalog
            self.doc_panel.remove_document_catalog(document_path)
            # Switch to the thumbnail view
            self.set_current_viewer(1)

    def setup_document_panel(self):
        """Setup the document panel."""
        self.doc_panel = DocumentPanel()
        self.layout.addWidget(self.doc_panel)
        self.layout.setCurrentIndex(0)

    def setup_thumbnail_panel(self):
        """Setup the thumbnail panel."""

        self.thumbnail_panel = ThumbnailPanel()
        self.layout.addWidget(self.thumbnail_panel)
        self.layout.setCurrentIndex(1)

    def get_document_panel(self) -> DocumentPanel:
        """Returns the document panel instance."""
        return self.doc_panel

    def set_current_viewer(self, index: int):
        """
        Sets the current viewer by index.

        Args:
            index (int): The index of the viewer to display.
        """
        self.layout.setCurrentIndex(index)

    def set_document(self, document_path: str):
        """
        Sets the current document to be displayed in the document panel.

        Args:
            document_path (str): The document to display.
        """
        self.doc_panel.set_document(document_path)

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
