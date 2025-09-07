# PySide6 Imports
from PySide6.QtPdf import (
    QPdfDocument,
)

# Project Imports
from .document import UIDocument

class PDFDocument(UIDocument, QPdfDocument):
    def __init__(self, file_path: str, parent=None):
        UIDocument.__init__(self, file_path)
        QPdfDocument.__init__(self, parent)
        self.load(file_path)