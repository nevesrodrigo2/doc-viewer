from PySide6.QtWidgets import QWidget, QHBoxLayout

from doc_viewer.frontend.events.event_bus import event_bus
from doc_viewer.frontend.windows.viewer.document_stack.doc_viewer_stack import DocumentViewerStack
from doc_viewer.frontend.windows.viewer.tab_group.tab_group import TabGroup

class MainDocumentPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # setup layout
        self.layout = QHBoxLayout()

        # setup tab group
        self.tab_group = TabGroup()
        self.layout.addWidget(self.tab_group, 1)

        # setup document viewer
        self.doc_viewer = DocumentViewerStack()
        self.layout.addWidget(self.doc_viewer, 5)
        self.layout.setSpacing(30)

        self.setLayout(self.layout)

        # setup events
        self.setup_events()

    def setup_events(self):
        """Setup event listeners."""
        # Subscribe to events
        event_bus.subscribe('files_added', self.add_files)
        event_bus.subscribe('document_changed', self.change_document)

    def add_document(self, document_path: str):
        """Add a document to the viewer and tab group."""
        print(f"Adding document: {document_path}")
        self.tab_group.load_document(document_path)
        self.doc_viewer.load_document(document_path)
        print(f"Document added: {document_path}")
        print(f"Current documents in tab group: {self.tab_group.doc_names}")
        print(f"Current documents in viewer stack: {self.doc_viewer.document_paths}")

    def change_document(self, document_name: str):
        """Change the currently displayed document by name."""
        print(f"Changing document to: {document_name}")
        self.doc_viewer.change_document(document_name)
        print(f"Document changed to: {document_name}")
        return
        
    def add_files(self, file_paths: list[str]):
        print(f"Files to add: {file_paths}")
        # Logic to handle added files, e.g., update the document viewer
        for file_path in file_paths:
            self.add_document(file_path)

        # Load the documents into the panel
        print("Files added to the document viewer.")
