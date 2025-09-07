# Project Imports
from doc_viewer.ui.components.tab_group.category.category import Category

class SmartCategory(Category):
    """
    A category that automatically includes documents based on a predicate function.
    """

    def __init__(self, name: str):
        super().__init__(name)
        