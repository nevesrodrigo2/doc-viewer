import pytest

from doc_viewer.domain.models.category.category_controller import CategoryController
from doc_viewer.domain.models.category.normal_category import NormalCategory
from doc_viewer.domain.models.category.smart_category import SmartCategory

@pytest.fixture
def normal_category():
    category = NormalCategory("Test Category")
    return category

@pytest.fixture
def smart_category():
    def predicate(doc):
        return doc.get_title() == "My PDF"

    category = SmartCategory("Test Smart Category", predicate)
    return category