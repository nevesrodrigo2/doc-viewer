from PySide6.QtWidgets import QHBoxLayout, QMainWindow, QWidget
from doc_viewer.frontend.windows.viewer.doc_viewer_widget import DocumentViewer
from doc_viewer.frontend.windows.menu_bar.menu_bar import MenuBar
from doc_viewer.frontend.windows.viewer.main_document_panel import MainDocumentPanel

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # setup main window
        self.setWindowTitle("Doc Viewer")
        self.resize(1280, 720)

        # setup menu bar
        self.menu_bar = MenuBar()
        self.setMenuBar(self.menu_bar)
        self.menu_bar.files_added.connect(self.add_files)
        # setup layout
        self.main_layout = QHBoxLayout()

        # setup document viewer 
        self.doc_window = MainDocumentPanel()
        
        # setup document tab group
        self.main_layout.addWidget(self.doc_window)

        # setup central widget
        widget = QWidget()
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)

    def add_files(self, file_paths):
        print(f"Files to add: {file_paths}")
        # Logic to handle added files, e.g., update the document viewer
        for file_path in file_paths:
            self.doc_window.add_document(file_path)
            self.doc_window.load_documents()
        print("Files added to the document viewer.")
