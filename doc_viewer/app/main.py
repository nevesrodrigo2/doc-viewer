import argparse

# PySide6
from PySide6.QtWidgets import QApplication

# Project Imports
from doc_viewer.settings.logger import get_logger
from doc_viewer.settings.config import APP_NAME
from doc_viewer.ui.main_window import MainWindow

from doc_viewer.domain.models.document import DocumentController
from doc_viewer.domain.models.folder import FolderController

# start logger
logger = get_logger(__name__)

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true', help='Run in debug mode')
args = parser.parse_args()

# document controller
doc_controller = DocumentController()

# folder controller
folder_controller = FolderController()

# setup ui
app = QApplication([])
window = MainWindow(APP_NAME)

app.exec()