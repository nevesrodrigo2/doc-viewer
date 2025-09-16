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
import logging 

parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true', help='Run in debug mode')
args = parser.parse_args()

# setup logger
level = logging.DEBUG if args.debug else logging.INFO
setup_logger(level=level)
logger = logging.getLogger(__name__)

class App():
    """Main application class."""
    def __init__(self, debug: bool = False):
    # Debug mode
        if debug:
            logger.debug("Running in debug mode")

        logger.info("Starting application...")

        # document controller
        self.doc_controller = DocumentController()

        # category controller
        self.category_controller = CategoryController()

        # setup ui
        app = QApplication([])
        self.window = MainWindow(APP_NAME)

        if debug:
            self.setup_debug_mode()

        app.exec()

    def setup_debug_mode(self):
        """Setup additional debug configurations."""
        logger.debug("Debug mode activated")
        self.window.setup_debug_mode()

def main():
    """Main entry point for the application."""
     # Parse command line arguments

    app = App(debug=args.debug)
