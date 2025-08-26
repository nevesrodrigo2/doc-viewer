import pytest
import os

from tests.config import PDF_TEMP_PATH

@pytest.fixture
def temp_path() -> str:
    return PDF_TEMP_PATH

def test_standard_pdf(document_controller, standard_pdf, temp_pdf_dir):
    assert document_controller.add_document(standard_pdf)
    doc = document_controller.get_documents()[standard_pdf]

    path = os.path.join(temp_pdf_dir, "standard.pdf")
    assert doc.get_file_path() == str(path)
    assert doc.get_title() == "My PDF"
    assert doc.get_author() == "Alice"
    assert doc.get_content() == "Hello World\n"
    assert doc.get_page_count() == 1

def test_empty_pdf(document_controller, empty_pdf, temp_pdf_dir):
    assert document_controller.add_document(empty_pdf)
    doc = document_controller.get_documents()[empty_pdf]

    path = os.path.join(temp_pdf_dir, "empty.pdf")
    assert doc.get_file_path() == str(path)
    assert doc.get_title() == "untitled"
    assert doc.get_author() == "anonymous"
    assert doc.get_content() == ""
    assert doc.get_page_count() == 1

def test_multi_page_pdf(document_controller, multi_page_pdf, temp_pdf_dir):
    assert document_controller.add_document(multi_page_pdf)
    doc = document_controller.get_documents()[multi_page_pdf]

    path = os.path.join(temp_pdf_dir, "multi.pdf")
    assert doc.get_file_path() == str(path)
    assert doc.get_title() == "Multi"
    assert doc.get_author() == "Bob"

    # test content
    content = ("Page 1\nPage 2\nPage 3\nPage 4\nPage 5\n")
    assert doc.get_content() == content
    assert doc.get_page_count() == 5

def test_is_favourited(document_controller, multi_page_pdf):
    assert document_controller.add_document(multi_page_pdf)
    doc = document_controller.get_documents()[multi_page_pdf]

    assert not doc.is_favourited()
    doc.set_favourite(True)
    assert doc.is_favourited()