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
from doc_viewer.ui.components.document_viewer.document_stack import DocumentViewerStack

class MainWindow(QMainWindow):
    """Main application window."""
    def __init__(self, app_name: str):
        super().__init__()
        self.setWindowTitle(app_name)

        self.setup_main_window()
        self.show()

    def setup_main_window(self):
        """Setup the main window layout and components."""

        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)

        # set menu bar
        self.menu_bar = MenuBar()
        self.layout.setMenuBar(self.menu_bar)

        # set main layout
        self.main_layout = QHBoxLayout()
        self.layout.addLayout(self.main_layout)

        # tab group
        self.tab_group = TabGroup()
        self.main_layout.addWidget(self.tab_group, 1)
        # document viewer stack
        self.doc_viewer_stack = DocumentViewerStack()
        self.main_layout.addWidget(self.doc_viewer_stack, 4)

