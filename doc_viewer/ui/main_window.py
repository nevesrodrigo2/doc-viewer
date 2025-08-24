from PySide6.QtWidgets import (
    QWidget, 
    QMainWindow, 
    QVBoxLayout, 
    QHBoxLayout
)

from doc_viewer.ui.components.menu_bar import MenuBar

class MainWindow(QMainWindow):
    def __init__(self, app_name: str):
        super().__init__()
        self.setWindowTitle(app_name)

        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create layout and assign it to the central widget
        self.layout = QVBoxLayout(central_widget)

        # set menu bar
        self.menu_bar = MenuBar()

        self.layout.setMenuBar(self.menu_bar)

        self.main_layout = QHBoxLayout()

        self.layout.addLayout(self.main_layout)