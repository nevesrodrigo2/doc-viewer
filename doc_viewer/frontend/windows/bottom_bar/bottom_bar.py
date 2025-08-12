from PySide6.QtWidgets import QHBoxLayout, QLabel, QWidget
from PySide6.QtCore import Signal
from doc_viewer.frontend.windows.bottom_bar.zoom.zoom_widget import ZoomWidget

class BottomBar(QWidget):
    """A widget representing the bottom bar of the document viewer."""
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)  # small gap

        self.zoom_widget = ZoomWidget()
        layout.addWidget(QLabel(""), 6)   # 6 parts
        layout.addWidget(self.zoom_widget, 1) # 1 part
    

