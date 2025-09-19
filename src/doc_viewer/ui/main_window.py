# PySide6 Imports
from PySide6.QtWidgets import (
    QWidget, 
    QMainWindow, 
    QVBoxLayout, 
    QHBoxLayout
)

# Project Imports
from doc_viewer.ui.components.menu_bar import MenuBar
from doc_viewer.ui.components.tab_group.tab_group import TabGroup
from doc_viewer.ui.main_panel import MainPanel
import doc_viewer.settings.config as config
from doc_viewer.domain.events.event_bus import event_bus
from doc_viewer.ui.events.document.ui_document_events import UIDocumentOpenedEvent

import os

class MainWindow(QMainWindow):
    """Main application window."""
    def __init__(self, app_name: str):
        super().__init__()
        self.setWindowTitle(app_name)

        self.setup_stylesheet()
        self.setup_main_window()
        self.show()

    def setup_stylesheet(self):
        """Load and apply all QSS files in QSS_PATH."""
        full_style = ""
        for style_file in os.listdir(config.QSS_PATH):
            if style_file.endswith(".qss"):
                with open(os.path.join(config.QSS_PATH, style_file), "r") as f:
                    full_style += f.read() + "\n"
        self.setStyleSheet(full_style)

    def setup_main_window(self):
        """Setup the main window layout and components."""

        # Create a central widget
        central_widget = QWidget()
        central_widget.setContentsMargins(0, 0, 0, 0)
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # set menu bar
        self.menu_bar = MenuBar()
        self.layout.setMenuBar(self.menu_bar)

        # set main layout
        self.main_layout = QHBoxLayout()
        self.layout.addLayout(self.main_layout)

        # add tab group and document viewer stack
        self.tab_group = TabGroup()
        self.main_layout.addWidget(self.tab_group, 1)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.main_panel = MainPanel()
        self.main_layout.addWidget(self.main_panel, 6)

        library = self.tab_group.tree_widget.library
        library_thumbnail_panel = library.get_thumbnail_panel()
        self.main_panel.set_thumbnail_panel(library_thumbnail_panel)

    def setup_debug_mode(self):
        """
        Setup additional debug configurations.
        
        Loads sample documents from the assets directory.
        """
        pdf_samples_path = config.PDF_DIR
        
        for file_path in os.listdir(pdf_samples_path):
            if file_path.endswith(".pdf"):
                full_path = os.path.join(pdf_samples_path, file_path)
                event = UIDocumentOpenedEvent(full_path)
                event_bus.emit(event)