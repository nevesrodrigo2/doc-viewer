from PySide6.QtWidgets import QWidget, QHBoxLayout

from doc_viewer.frontend.windows.viewer.doc_viewer_stack import DocumentViewerStack
from doc_viewer.frontend.windows.viewer.tab_group import TabGroup

class MainDocumentPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # setup documents
        self.documents = []
        self.current_document = None
        
        # setup layout
        self.layout = QHBoxLayout()

        # setup tab group
        self.tab_group = TabGroup(self.documents)
        
        self.layout.addWidget(self.tab_group, 1)

        # setup document viewer
        self.doc_viewer = DocumentViewerStack(self.documents)
        self.layout.addWidget(self.doc_viewer, 5)
        self.layout.setSpacing(50)

        self.setLayout(self.layout)

    def add_document(self, document_path: str):
        if document_path not in self.documents:
            self.documents.append(document_path)
            print(f"Document added: {document_path}")
        else:
            print(f"Document already exists: {document_path}")

    def load_documents(self):
        self.tab_group.load_documents()
        self.doc_viewer.load_documents()
        print("Documents loaded in the main document panel.")