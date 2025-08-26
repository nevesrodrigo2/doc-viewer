import pytest

from doc_viewer.domain.models.document.document_controller import DocumentController

def test_add_document(document_controller, standard_pdf):
    assert document_controller.add_document(standard_pdf)
    assert len(document_controller.get_documents()) == 1

def test_remove_document(document_controller, standard_pdf):
    document_controller.add_document(standard_pdf)
    assert len(document_controller.get_documents()) == 1
    assert document_controller.remove_document(standard_pdf)
    assert len(document_controller.get_documents()) == 0
    # Try to remove from empty list
    assert not document_controller.remove_document(standard_pdf)

def test_get_documents(document_controller, standard_pdf, empty_pdf):
    assert len(document_controller.get_documents()) == 0
    document_controller.add_document(standard_pdf)
    assert len(document_controller.get_documents()) == 1
    document_controller.add_document(empty_pdf)
    assert len(document_controller.get_documents()) == 2

def test_is_favourited(document_controller, standard_pdf, empty_pdf):
    document_controller.add_document(standard_pdf)
    document_controller.add_document(empty_pdf)
    assert not document_controller.is_favourited(standard_pdf)
    assert not document_controller.is_favourited(empty_pdf)
    # Invalid index
    assert not document_controller.is_favourited("invalid_path")

def test_set_favourite(document_controller, standard_pdf):
    document_controller.add_document(standard_pdf)
    assert document_controller.set_favourite(standard_pdf, True)
    assert document_controller.is_favourited(standard_pdf)