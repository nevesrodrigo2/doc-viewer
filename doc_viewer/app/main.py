import argparse

# PySide6 Imports
from PySide6.QtWidgets import QApplication

# Project Imports
from doc_viewer.settings.config import APP_NAME
from doc_viewer.ui.main_window import MainWindow

from doc_viewer.domain.models.document.document_controller import DocumentController
from doc_viewer.domain.models.category.category_controller import CategoryController

# Start logger with color formatting
from doc_viewer.settings.logger import setup_logger
setup_logger()

import logging 
logger = logging.getLogger(__name__)

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true', help='Run in debug mode')
args = parser.parse_args()

logger.info("Starting application...")

# document controller
doc_controller = DocumentController()

# category controller
category_controller = CategoryController()

# setup ui
app = QApplication([])
window = MainWindow(APP_NAME)

app.exec()