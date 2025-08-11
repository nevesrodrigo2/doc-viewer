from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGraphicsView

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('doc-viewer')
        self.resize(1920,1080)
        #layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        #widgets
        self.docViewer = QGraphicsView()
        layout.addWidget(self.docViewer)
