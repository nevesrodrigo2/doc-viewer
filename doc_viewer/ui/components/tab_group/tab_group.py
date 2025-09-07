# PySide6 Imports
from PySide6.QtWidgets import (
    QWidget, 
    QVBoxLayout, 
)

# Project Imports
from doc_viewer.ui.components.tab_group.tree_widget import TreeWidget
from doc_viewer.ui.components.tab_group.document_counter import DocumentCounter

class TabGroup(QWidget):
    """A widget that contains a group of tabs."""
    def __init__(self):
        super().__init__()
        # Initialize tab group UI components here

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        # add tree widget and document counter
        self.tree_widget = TreeWidget()
        self.layout.addWidget(self.tree_widget, 4)
        
        # add document counter
        self.document_counter = DocumentCounter()
        self.layout.addWidget(self.document_counter, 1)
