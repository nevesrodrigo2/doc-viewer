import fitz  # PyMuPDF
from doc_viewer.backend.models.document.Document import Document

class PDFDocument(Document):
    def __init__(self, file_path: str):
        super().__init__(file_path)
        self.extension = "docx"

    def load_document(self):
        # Logic to load a PDF document
        self.doc = fitz.open(self.file_path) 
        self.pages = [page for page in self.doc]