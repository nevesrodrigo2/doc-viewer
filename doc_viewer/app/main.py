import argparse
from doc_viewer.settings import config
from doc_viewer.settings.config import set_debug, load_debug_settings
from doc_viewer.frontend.events.event_bus import EventBus
from PySide6.QtWidgets import QApplication
from doc_viewer.frontend.windows.main_window import MainWindow

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true', help='Run in debug mode')
args = parser.parse_args()

# SETUP DEBUG MODE
set_debug(args.debug)
if args.debug:
    # Implement loggin later
    print("Running in debug mode")
    load_debug_settings()
    print(f"Debug settings loaded: {config.settings}")
else:
    print("Running in normal mode")

app = QApplication([])
window = MainWindow()
window.show()

app.exec()