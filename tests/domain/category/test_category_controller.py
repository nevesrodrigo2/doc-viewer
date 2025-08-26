def test_add_normal_category(category_controller):
    result = category_controller.add_normal_category("Test Category")
    assert result is True
    assert len(category_controller.get_categories()) == 3
    assert "Test Category" in category_controller.get_categories()

def test_add_smart_category(category_controller):
    def predicate(doc):
        return doc.get_title() == "Test Document"

    result = category_controller.add_smart_category("Test Smart Category", predicate)
    assert result is True
    assert len(category_controller.get_categories()) == 3
    assert "Test Smart Category" in category_controller.get_categories()

def test_remove_category(category_controller):
    false_result = category_controller.remove_category("Test Category")
    assert false_result is False

    category_controller.add_normal_category("Test Category")
    result = category_controller.remove_category("Test Category")
    assert result is True

def test_add_document(category_controller, standard_document):
    category_controller.add_normal_category("Test Category")
    result = category_controller.add_document("Test Category", standard_document)
    assert result is True
