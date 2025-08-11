from PySide6.QtWidgets import QWidget, QStackedLayout

from doc_viewer.frontend.windows.viewer.doc_viewer_widget import DocumentViewer

class DocumentViewerStack(QWidget):
    def __init__(self, documents):
        super().__init__()
        self.documents = documents
        
        # setup layout for the document viewer stack
        self.layout = QStackedLayout()
        self.load_documents()
        
        self.setLayout(self.layout)

    def load_documents(self):
        for doc in self.documents:
            viewer = DocumentViewer(doc)
            self.layout.addWidget(viewer)
        
        if self.documents:
            self.layout.setCurrentIndex(0)