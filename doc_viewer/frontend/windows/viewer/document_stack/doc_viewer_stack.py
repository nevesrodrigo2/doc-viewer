from PySide6.QtWidgets import QWidget, QStackedLayout

from doc_viewer.frontend.windows.viewer.document_stack.doc_viewer_widget import DocumentViewer

class DocumentViewerStack(QWidget):
    """A widget that manages a stack of document viewers."""
    def __init__(self):
        super().__init__()
        self.document_paths = []
        
        # setup layout for the document viewer stack
        self.layout = QStackedLayout()
        self.layout.setCurrentIndex(0)
        self.setLayout(self.layout)

    def load_document(self, document_path):
        """Load a document into the stacked layout."""

        if document_path not in self.document_paths:
            self.document_paths.append(document_path)
            print(f"Document loaded: {document_path}")
            viewer = DocumentViewer(document_path)
            self.layout.addWidget(viewer)
            self.layout.setCurrentIndex(len(self.document_paths) - 1)
        else:
            print(f"Document already loaded: {document_path}")
            
    def change_document(self, document_name):
        """Change the currently displayed document by name."""
        for document_path in self.document_paths:
            if document_path.rsplit('/', 1)[-1] == document_name:
                index = self.document_paths.index(document_path)
                self.layout.setCurrentIndex(index)
                print(f"Document changed to: {document_name}")
                return
        print(f"Document not found: {document_name}")