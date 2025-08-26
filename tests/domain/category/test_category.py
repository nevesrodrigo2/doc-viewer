from doc_viewer.domain.models.document.document_factory import DocumentFactory

# NORMAL CATEGORY TESTS
def test_add_document(normal_category, standard_document):

    result = normal_category.add_document(standard_document)
    assert result is True
    assert len(normal_category.get_documents()) == 1
    assert normal_category.get_documents()[0].get_title() == "My PDF"

def test_add_document_failure(normal_category, standard_document):
    # Simulate a failure scenario
    normal_category.add_document(standard_document)
    result = normal_category.add_document(standard_document)
    assert result is False
    assert len(normal_category.get_documents()) == 1

def test_remove_document(normal_category, standard_document):

    normal_category.add_document(standard_document)
    result = normal_category.remove_document(standard_document)
    assert result is True
    assert len(normal_category.get_documents()) == 0

def test_remove_document_failure(normal_category, standard_document):
    # Simulate a failure scenario
    result = normal_category.remove_document(standard_document)
    assert result is False
    assert len(normal_category.get_documents()) == 0

# SMART CATEGORY TESTS
def test_smart_category_add_document(smart_category, standard_document):
    result = smart_category.add_document(standard_document)
    assert result is True
    assert len(smart_category.get_documents()) == 1
    assert smart_category.get_documents()[0].get_title() == "My PDF"

def test_smart_category_add_document_failure(smart_category, empty_document):
    # Simulate a failure scenario
    result = smart_category.add_document(empty_document)
    assert result is False
    assert len(smart_category.get_documents()) == 0