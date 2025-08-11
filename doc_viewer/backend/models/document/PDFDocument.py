import fitz  # PyMuPDF
from doc_viewer.backend.models.document.Document import Document
from doc_viewer.backend.models.document.Page import Page

class PDFDocument(Document):
    def __init__(self, file_path: str):
        super().__init__(file_path)
        self.extension = "docx"

    def load_document(self):
        # Logic to load a PDF document
        self.doc = fitz.open(self.file_path) 
        for page in self.doc:
            # create new page with the page from the doc object 
            # and append it to the list
            self.pages.append(Page(page)) 
