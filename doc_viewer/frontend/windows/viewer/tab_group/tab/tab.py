from PySide6.QtWidgets import QLabel, QSizePolicy

class Tab(QLabel):

    """A widget representing a single tab in the document viewer."""
    def __init__(self, document_name):
        super().__init__(document_name)
        self.document_name = document_name
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    def get_doc_name(self):
        """Return the name of the document associated with this tab."""
        return self.document_name