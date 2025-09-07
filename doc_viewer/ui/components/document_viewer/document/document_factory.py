# PySide6 Imports

# Project Imports
from .document import UIDocument
from .pdf_document import PDFDocument
from .docx_document import DOCXDocument

class DocumentFactory:

    @staticmethod
    def create_document(file_path: str) -> UIDocument:
        if file_path.lower().endswith('.pdf'):
            return PDFDocument(file_path)
        elif file_path.lower().endswith('.docx'):
            return DOCXDocument(file_path)
        else:
            raise ValueError(f"Unsupported file type for file: {file_path}")