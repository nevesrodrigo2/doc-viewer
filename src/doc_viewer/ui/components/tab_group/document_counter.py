# PySide6 Imports
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
)

# Project Imports
from doc_viewer.ui.components.document_viewer.document_catalog import document_catalog
from doc_viewer.domain.events.event_bus import event_bus
from doc_viewer.domain.events.document.document_events import (
    DocumentAddedEvent,
    DocumentRemovedEvent
)

class DocumentCounter(QWidget):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        self.count = 0
        self.counter_label = QLabel(f"Files: {self.count} Documents")
        self.counter_label.setObjectName("DocumentCounter")

        self.layout.addWidget(self.counter_label)

        self.subscribe_events()

    def subscribe_events(self):
        """Subscribe to relevant document events."""
        event_bus.subscribe(DocumentAddedEvent, self.handle_events)
        event_bus.subscribe(DocumentRemovedEvent, self.handle_events)

    def handle_events(self, event):
        """Handle document events and update the counter."""
        self.update_counter_label()

    def update_counter_label(self):
        """
        Update the counter label with the current count.
        self.counter_label.setText(f"Files: {self.count} Documents")
        """
        count = document_catalog.get_document_count()

        self.counter_label.setText(f"Files: {count} Documents")