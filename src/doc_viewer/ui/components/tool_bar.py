# PySide6 Imports
from PySide6.QtWidgets import (
    QToolBar,
)
from PySide6.QtGui import (
    QAction,
    QIcon,
)
# Project Imports
from doc_viewer.domain.events.event_bus import event_bus
from doc_viewer.ui.events.toolbar.toolbar_events import (
    ToolBarToggleFavouriteEvent,
    ToolBarDeleteDocumentEvent
)
import doc_viewer.settings.config as config

import logging
logger = logging.getLogger(__name__)

class ToolBar(QToolBar):
    """
    Custom ToolBar for the application.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("ToolBar")
        self.setup_actions()

    def setup_actions(self):
        # Favouriting a document
        self.favourite_action = QAction(
            QIcon(config.ICON_PATH + "heart.png"), 
            "Favourite", self
        )
        self.favourite_action.setCheckable(True)
        self.favourite_action.triggered.connect(self.toggle_favourite)
        self.addAction(self.favourite_action)

        # Deleting a document
        self.delete_action = QAction(
            QIcon(config.ICON_PATH + "delete.png"), 
            "Delete", self
        )
        self.delete_action.triggered.connect(self.delete_document)
        self.addAction(self.delete_action)

    def toggle_favourite(self, checked):
        """
        Toggle the favourite status of the current document.
        """

        # Emit event to toggle favourite status
        event_bus.emit(ToolBarToggleFavouriteEvent())

    def delete_document(self):
        """
        Placeholder for delete document functionality.
        """
        event_bus.emit(ToolBarDeleteDocumentEvent())

    def update_toolbar_state(self, is_favourited: bool = False):
        """
        Update the toolbar state based on the current document's properties.

        Args:
            is_favourited (bool): Whether the current document is favourited.
        """

        # For now the only state we manage is the favourite status
        self.favourite_action.setChecked(is_favourited)