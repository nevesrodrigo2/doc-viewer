import sys

# PySide6 Imports
from PySide6.QtWidgets import (
    QMenuBar,
    QFileDialog,
)
from PySide6.QtGui import (
    QAction,
)
from PySide6.QtCore import (
    QStandardPaths,
)

# Project Imports
import logging
from doc_viewer.ui.events.document.ui_document_events import (
    UIDocumentOpenedEvent,
    UIDocumentEvent,
)
from doc_viewer.domain.events.event_bus import event_bus

logger = logging.getLogger(__name__)

class MenuBar(QMenuBar):
    """Menu bar for the application."""
    def __init__(self):
        super().__init__()
        self.setup_bar()

    def emit_event(self, event: UIDocumentEvent):
        """Emit an event to the event bus."""
        event_bus.emit(event)
        
    def setup_bar(self):
        """Setup the menu bar with predefined menus and actions."""
        menus = [
            ("File", ["Open", "Save", "Exit"]),
            ("Edit", ["Undo", "Redo", "Copy", "Paste"]),
            ("View", ["Zoom In", "Zoom Out"]),
            ("Help", ["About", "Keyboard Shortcuts"])
        ]

        for menu_name, actions in menus:
            menu = self.addMenu(menu_name)
            for action in actions:
                menu_action = self.setup_actions(action)
                menu.addAction(menu_action)


    def setup_actions(self, action: str) -> QAction:
        """Setup actions for the menu items."""
        menu_action = QAction(action, self)
        if action == "Open":
            menu_action.triggered.connect(self.open_action)
        elif action == "Exit":
            menu_action.triggered.connect(self.close_action)
        return menu_action

    def open_action(self):
        """Handle the Open action."""

        logger.debug("Open action triggered.")

        # set default documents location
        documents_location = QStandardPaths.writableLocation(
            QStandardPaths.DocumentsLocation
        )

        # Open file dialog to select documents
        file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            "Select one or more files to open",
            documents_location,
            "Documents (*.pdf *.docx *.txt)"
        )

        if not file_paths:
            logger.debug("No files were selected.")

        for path in file_paths:
            logger.debug(f"Selected file: {path}")
            # Emit document opened event
            event = UIDocumentOpenedEvent(path)
            self.emit_event(event)

    def close_action(self):
        """Handle the Exit action."""
        logger.debug("Exit action triggered.")
        sys.exit()  

