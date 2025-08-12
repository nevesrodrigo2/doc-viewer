from PySide6.QtWidgets import QWidget, QStackedLayout

from doc_viewer.frontend.windows.viewer.document_stack.doc_viewer_widget import DocumentViewer

class DocumentViewerStack(QWidget):
    """A widget that manages a stack of document viewers."""
    def __init__(self, documents):
        super().__init__()
        self.documents = documents
        
        # setup layout for the document viewer stack
        self.layout = QStackedLayout()
        self.load_documents()
        
        self.setLayout(self.layout)

    def load_documents(self):
        """Load documents into the stacked layout."""
        for doc in self.documents:
            viewer = DocumentViewer(doc)
            self.layout.addWidget(viewer)
        
        if self.documents:
            self.layout.setCurrentIndex(0)

    def change_document(self, index):
        """Change the currently displayed document by index."""
        if 0 <= index < self.layout.count():
            self.layout.setCurrentIndex(index)
        else:
            raise IndexError("Index out of range for document viewer stack.")