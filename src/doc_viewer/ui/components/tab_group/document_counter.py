# PySide6 Imports
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
)

# Project Imports


class DocumentCounter(QWidget):
    """
    A widget that displays the count of documents.
    """
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        total_label = QLabel("Total: ")
        self.layout.addWidget(total_label)

        self.counter_label = QLabel("0 Documents")
        self.layout.addWidget(self.counter_label)

