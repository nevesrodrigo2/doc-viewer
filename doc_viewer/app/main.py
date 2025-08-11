from PyQt6.QtWidgets import QApplication
from doc_viewer.frontend.windows.main_window import MainWindow

app = QApplication([])
window = MainWindow()
window.show()

app.exec()