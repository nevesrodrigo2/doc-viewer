# DOCUMENT ADD TESTS

def test_document_added_event(document_controller, category_controller, standard_pdf):
    document_controller.add_document(standard_pdf)
    document = document_controller.get_documents()[standard_pdf]
    recents_cat = category_controller.get_category("Recents")

    docs = recents_cat.get_documents()
    assert len(docs) == 1
    assert docs == [document]

def test_document_added_multiple_recents_event(document_controller, category_controller, standard_pdf, empty_pdf):
    document_controller.add_document(standard_pdf)
    standard_doc = document_controller.get_documents()[standard_pdf]
    recents_cat = category_controller.get_category("Recents")

    recent_docs = recents_cat.get_documents()
    assert len(recent_docs) == 1
    assert recent_docs == [standard_doc]

    document_controller.add_document(empty_pdf)
    empty_doc = document_controller.get_documents()[empty_pdf]
    recent_docs = recents_cat.get_documents()
    print(recent_docs)
    assert len(recent_docs) == 2
    assert recent_docs == [empty_doc, standard_doc]

# DOCUMENT REMOVE TESTS
def test_document_removed_event(document_controller, category_controller, standard_pdf):
    document_controller.add_document(standard_pdf)
    document = document_controller.get_documents()[standard_pdf]
    category_controller.add_normal_category("TestCategory")
    category_controller.add_document("TestCategory", document)
    document_controller.remove_document(standard_pdf)

    # Check that the document is removed from the category
    assert category_controller.get_category("TestCategory").get_documents() == []

def test_document_removed_multiple_categories_event(document_controller, category_controller, standard_pdf):
    document_controller.add_document(standard_pdf)
    document = document_controller.get_documents()[standard_pdf]
    category_controller.add_normal_category("TestCategory")
    category_controller.add_normal_category("TestCategory2")
    category_controller.add_document("TestCategory", document)
    category_controller.add_document("TestCategory2", document)
    document_controller.remove_document(standard_pdf)

    # Check that the document is removed from the category
    assert category_controller.get_category("TestCategory").get_documents() == []
    assert category_controller.get_category("TestCategory2").get_documents() == []
    assert category_controller.get_category("Recents").get_documents() == []

# DOCUMENT FAVOURITE TESTS
def test_document_favourited_event(document_controller, category_controller, standard_pdf):

    document_controller.add_document(standard_pdf)
    document_controller.set_favourite(standard_pdf)

    fav_documents = category_controller.get_category("Favourites").get_documents()
    assert len(fav_documents) == 1
    fav_document = fav_documents[0]
    assert fav_document.get_file_path() == standard_pdf

def test_document_unfavourited_event(document_controller, category_controller, standard_pdf):

    document_controller.add_document(standard_pdf)
    document_controller.set_favourite(standard_pdf)
    fav_documents = category_controller.get_category("Favourites").get_documents()

    assert len(fav_documents) == 1
    document_controller.set_favourite(standard_pdf)

    assert len(fav_documents) == 0 

def test_document_favourited_recents_event(document_controller, category_controller, standard_pdf, empty_pdf):

    document_controller.add_document(standard_pdf)
    document_controller.add_document(empty_pdf)

    standard_doc = document_controller.get_document(standard_pdf)
    empty_doc = document_controller.get_document(empty_pdf)

    recent_cat = category_controller.get_category("Recents")
    recents_documents = recent_cat.get_documents()

    assert recents_documents == [empty_doc, standard_doc]

    document_controller.set_favourite(standard_pdf)

    recents_documents = recent_cat.get_documents()
    assert recents_documents == [standard_doc, empty_doc]

def test_document_unfavourited_recents_event(document_controller, category_controller, standard_pdf, empty_pdf):

    document_controller.add_document(standard_pdf)
    document_controller.add_document(empty_pdf)

    standard_doc = document_controller.get_document(standard_pdf)
    empty_doc = document_controller.get_document(empty_pdf)

    recent_cat = category_controller.get_category("Recents")
    recents_documents = recent_cat.get_documents()

    assert recents_documents == [empty_doc, standard_doc]

    document_controller.set_favourite(standard_pdf)
    document_controller.set_favourite(empty_pdf)

    recents_documents = recent_cat.get_documents()
    assert recents_documents == [empty_doc, standard_doc]

    document_controller.set_favourite(standard_pdf)

    recents_documents = recent_cat.get_documents()
    assert recents_documents == [standard_doc, empty_doc]
