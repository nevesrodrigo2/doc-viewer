
from doc_viewer.backend.models.document.DOCXDocument import DOCXDocument        
from doc_viewer.backend.models.document.PDFDocument import PDFDocument        
from doc_viewer.backend.models.document.TextDocument import TextDocument        


extensions = ["pdf", "docx", "txt"]

class DocumentFactory:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.extension = self.get_file_extension()
        self.document = self.create_document()

    def get_file_extension(self) -> str:
        return self.file_path.split('.')[-1].lower()
    
    def create_document(self):
        if self.extension == "pdf":
            return PDFDocument(self.file_path)
        elif self.extension == "docx":
            return DOCXDocument(self.file_path)
        elif self.extension == "txt":
            return TextDocument(self.file_path)
        else:
            raise ValueError(f"Unsupported file type: {self.extension}")