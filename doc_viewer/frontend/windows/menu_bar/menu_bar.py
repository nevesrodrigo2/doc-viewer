from PySide6.QtWidgets import QMenuBar, QFileDialog
from PySide6.QtGui import QAction
from PySide6.QtCore import Signal

from doc_viewer.frontend.events.event_bus import event_bus

class MenuBar(QMenuBar):

    # files_added = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.file_menu = self.addMenu("File")
        self.option_menu = self.addMenu("Edit")
        self.view_menu = self.addMenu("View")
        self.window_menu = self.addMenu("Window")
        self.help_menu = self.addMenu("Help")

        self.setup_file_menu()

    def setup_file_menu(self):
        add_btn = QAction("Add File", self)
        add_btn.triggered.connect(self.add_file)
        self.file_menu.addAction(add_btn)

    def add_file(self):
        # Logic to add a file goes here
        print("Add File action triggered")
        file_paths, _ = QFileDialog.getOpenFileNames(
            self,                        # Parent widget
            "Select a file",             # Dialog title
            "",                           # Starting directory ("" means current)
            "All Files (*);;Text Files (*.txt);;PDF Files (*.pdf);; Document Files (*.docx)"  # File filters
        )
        if file_paths:
            print(f"Selected files: {file_paths}")
            # self.files_added.emit(file_paths)
            self.emit_event('files_added', file_paths)

    def emit_event(self, event_name, *args, **kwargs):
        """Send an event to the event bus."""
        event_bus.emit(event_name, *args, **kwargs)
        print(f"Event '{event_name}' emitted with args: {args} and kwargs: {kwargs}")