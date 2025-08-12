from PySide6.QtWidgets import QLabel, QSizePolicy
from PySide6.QtGui import QFontMetrics
from PySide6.QtCore import Qt

class Tab(QLabel):

    """A widget representing a single tab in the document viewer."""
    def __init__(self, document_name):
        super().__init__(document_name)
        self.document_name = document_name
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        # Set tool tip for the tab
        self.setToolTip(document_name)
        self.setToolTipDuration(1000)  # Show tooltip for 1000 milliseconds

    def get_doc_name(self):
        """Return the name of the document associated with this tab."""
        return self.document_name
    
    def get_elided_text(self, document_name):
        """Return the elided text for the document name."""
        font_metrics = QFontMetrics(self.font())
        print(f"width of label: {self.width()}")
        elided_text = font_metrics.elidedText(document_name, Qt.ElideRight, self.width())
        print(f"Elided text for '{document_name}': '{elided_text}'")
        return elided_text
    
    def resizeEvent(self, event):
        """Handle resize events to update the elided text."""
        elided = self.get_elided_text(self.document_name)
        self.setText(elided)
        super().resizeEvent(event)