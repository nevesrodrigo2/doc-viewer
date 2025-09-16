# PySide6 imports
from PySide6.QtWidgets import (
    QTreeWidget,
    QTreeWidgetItem,
)

# Project Imports
from doc_viewer.ui.components.tab_group.category.category import Category
from doc_viewer.ui.components.tab_group.category.smart_category import SmartCategory
from doc_viewer.ui.components.tab_group.library.library import Library

import doc_viewer.settings.config as config 

class TreeWidget(QTreeWidget):
    def __init__(self):
        super().__init__()
        
        self.setHeaderHidden(True)
        self.library = Library()
        self.addTopLevelItem(self.library)

        self.categories_list = []

        self.categories = QTreeWidgetItem(["Categories"])
        self.addTopLevelItem(self.categories)
        self.setup_smart_categories()

        # sets all items expanded
        self.expandAll()

        # 👇 Connect tree’s double-click signal once
        self.itemDoubleClicked.connect(self.on_item_double_clicked)

    def on_item_double_clicked(self, item: QTreeWidgetItem):
        """
        Handle double-click event on tree items.
        Emits an event to notify other components.

        Args:
            item (QTreeWidgetItem): The item that was double-clicked.
            column (int): The column index that was clicked.
        """
        if hasattr(item, "on_double_click"):
            item.on_double_click()

    def setup_smart_categories(self):
        """
        Setup smart categories in the tree widget.

        Categories include:
        - Recents
        - Favorites
        """

        self.recents_category = SmartCategory(config.RECENTS_CATEGORY_NAME)
        self.categories.addChild(self.recents_category)
        self.categories_list.append(config.RECENTS_CATEGORY_NAME)

        self.favorites_category = SmartCategory(config.FAVOURITES_CATEGORY_NAME)
        self.categories.addChild(self.favorites_category)
        self.categories_list.append(config.FAVOURITES_CATEGORY_NAME)

    def add_category(self, category_name: str) -> bool:
        """
        Add a new category to the tree widget.

        Args:
            category_name (str): The name of the category to add.

        Returns:
            bool: True if the category was added successfully, False otherwise.
        """
        if not category_name:
            return False

        new_category = Category(category_name)
        self.categories.addChild(new_category)
        return True