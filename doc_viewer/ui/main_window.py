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