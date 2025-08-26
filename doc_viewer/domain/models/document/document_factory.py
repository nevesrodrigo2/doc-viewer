import pymupdf
import logging

from .document import Document

logger = logging.getLogger(__name__)  

class DocumentFactory:
    @staticmethod
    def create_document(file_path: str) -> Document:
        """
        Create a document from the given file path.

        Args:
            file_path (str): The path to the document file.

        Returns:
            Document: The created document.
        """

        # Logic to create a Document instance from the file
        try:
            ext = file_path.split('.')[-1].lower()
        except:
            logger.error("File path does not have an extension.")
            ext = ''

        if ext == 'txt':
            return DocumentFactory.create_txt_document(file_path)
        elif ext == 'pdf':
            return DocumentFactory.create_pdf_document(file_path)
        elif ext == 'docx':
            return DocumentFactory.create_docx_document(file_path)
        else:
            raise ValueError(f"Unsupported file type: {ext}")

    @staticmethod
    def create_pdf_document(file_path: str) -> Document:
        """
        Create a PDF document.

        Args:
            file_path (str): The path to the PDF file.

        Returns:
            Document: The created PDF document.
        """
        doc = pymupdf.open(file_path)
        return Document(doc, file_path)
    
    @staticmethod
    def create_docx_document(file_path: str) -> Document:
        """
        Create a DOCX document.

        Args:
            file_path (str): The path to the DOCX file.

        Returns:
            Document: The created DOCX document.
        """
        doc = DocumentFactory.open_docx(file_path)
        return Document(doc, file_path)

    @staticmethod
    def create_txt_document(file_path: str) -> Document:
        """
        Create a TXT document.

        Args:
            file_path (str): The path to the TXT file.

        Returns:
            Document: The created TXT document.
        """
        doc = DocumentFactory.open_txt(file_path)
        return Document(doc, file_path)