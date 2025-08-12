from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QMainWindow, QWidget, QLabel
from PySide6.QtCore import Qt

from doc_viewer.frontend.windows.menu_bar.menu_bar import MenuBar
from doc_viewer.frontend.windows.viewer.main_document_panel import MainDocumentPanel
from doc_viewer.frontend.windows.bottom_bar.bottom_bar import BottomBar
from doc_viewer.frontend.events.event_bus import event_bus
import doc_viewer.settings.config as config
import os

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # setup main window
        self.setWindowTitle("Doc Viewer")
        self.resize(1280, 720)

        # setup menu bar
        self.menu_bar = MenuBar()
        self.setMenuBar(self.menu_bar)
        # self.menu_bar.files_added.connect(self.add_files)

        

        self.outer_layout = QVBoxLayout()
        # setup layout
        self.document_layout = QHBoxLayout()

        # setup document viewer 
        self.doc_panel = MainDocumentPanel()
        
        # setup document tab group
        self.document_layout.addWidget(self.doc_panel)

        # Bottom bar
        self.outer_layout.addLayout(self.document_layout)
        self.bottom_bar = BottomBar()
        self.outer_layout.addWidget(self.bottom_bar)

        # setup central widget
        widget = QWidget()
        widget.setLayout(self.outer_layout)
        self.setCentralWidget(widget)

        # debug mode
        if config.debug:
            self.setup_debug_mode()

    def setup_debug_mode(self):
        print("Setting up debug mode...")
        pdf_path_dir = config.settings.get('pdf_path_dir', '')
        if pdf_path_dir:
            print(f"PDF Path Directory: {pdf_path_dir}")
            file_paths = []
            if os.path.exists(pdf_path_dir):
                for file_path in os.listdir(pdf_path_dir):
                    print(f"Checking file: {file_path}")
                    full_path = os.path.join(pdf_path_dir, file_path)
                    if os.path.isfile(full_path) and full_path.endswith('.pdf'):
                        file_paths.append(full_path)
            self.doc_panel.add_files(file_paths)

    
