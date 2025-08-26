# DOCUMENT ADD TESTS

## IMPORTANT 
# I don't know if this test will always work. I still need to implement
# the predicate for Recents Category
def test_document_added_event(document_controller, category_controller, standard_pdf):
    document_controller.add_document(standard_pdf)
    document = document_controller.get_documents()[standard_pdf]
    recents_cat = category_controller.get_category("Recents")

    docs = recents_cat.get_documents()
    assert len(docs) == 1
    assert docs == [document]

# DOCUMENT REMOVE TESTS
def test_document_removed_event(document_controller, category_controller, standard_pdf):
    document_controller.add_document(standard_pdf)
    document = document_controller.get_documents()[standard_pdf]
    category_controller.add_normal_category("TestCategory")
    category_controller.add_document("TestCategory", document)
    document_controller.remove_document(standard_pdf)

    # Check that the document is removed from the category
    assert category_controller.get_category("TestCategory").get_documents() == []

# DOCUMENT FAVOURITE TESTS
def test_document_favourited_event(document_controller, category_controller, standard_pdf):

    document_controller.add_document(standard_pdf)
    document_controller.set_favourite(standard_pdf, True)

    fav_documents = category_controller.get_category("Favourites").get_documents()
    assert len(fav_documents) == 1
    fav_document = fav_documents[0]
    assert fav_document.get_file_path() == standard_pdf

def test_document_unfavourited_event(document_controller, category_controller, standard_pdf):

    document_controller.add_document(standard_pdf)
    document_controller.set_favourite(standard_pdf, True)
    fav_documents = category_controller.get_category("Favourites").get_documents()

    assert len(fav_documents) == 1
    document_controller.set_favourite(standard_pdf, False)

    assert len(fav_documents) == 0 