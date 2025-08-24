import argparse

# PySide6
from PySide6.QtWidgets import QApplication

# Project Imports
from doc_viewer.settings.logger import get_logger
from doc_viewer.settings.config import APP_NAME
from doc_viewer.ui.main_window import MainWindow

# start logger
logger = get_logger(__name__)

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true', help='Run in debug mode')
args = parser.parse_args()

app = QApplication([])
window = MainWindow(APP_NAME)
window.show()

app.exec()