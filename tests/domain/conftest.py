import pytest
from pathlib import Path

from doc_viewer.domain.models.category.category_controller import CategoryController
from doc_viewer.domain.models.document.document_controller import DocumentController
from doc_viewer.domain.models.document.document_factory import DocumentFactory

from .document.mock_document import (
    create_mock_pdf, 
    create_empty_pdf, 
    create_multi_page_pdf
)

@pytest.fixture
def document_controller():
    document_controller = DocumentController()
    return document_controller

@pytest.fixture
def category_controller():
    return CategoryController()
    
@pytest.fixture
def standard_document(temp_pdf_dir, standard_pdf):
    doc = DocumentFactory.create_document(standard_pdf)
    return doc

@pytest.fixture
def empty_document(temp_pdf_dir, empty_pdf):
    doc = DocumentFactory.create_document(empty_pdf)
    return doc

@pytest.fixture(scope="session")
def temp_pdf_dir():
    # Create a temporary directory for all PDFs
    import tempfile, shutil
    temp_dir = tempfile.mkdtemp(prefix="pytest_pdfs_")
    path = Path(temp_dir)
    yield path
    shutil.rmtree(temp_dir)

@pytest.fixture
def standard_pdf(temp_pdf_dir, filename="standard.pdf", title="My PDF", author="Alice", content="Hello World"):
    """Standard PDF with title, author, and content, saved in temp dir."""
    return create_mock_pdf(temp_pdf_dir, filename=filename, title=title, author=author, content=content)

@pytest.fixture
def empty_pdf(temp_pdf_dir, filename="empty.pdf"):
    """Completely empty PDF with no metadata, saved in temp dir."""
    return create_empty_pdf(temp_pdf_dir, filename=filename)

@pytest.fixture
def multi_page_pdf(temp_pdf_dir, filename="multi.pdf", num_pages=5, title="Multi", author="Bob"):
    """PDF with multiple pages, saved in temp dir."""
    return create_multi_page_pdf(temp_pdf_dir, filename=filename, num_pages=num_pages, title=title, author=author)
3