import logging
from  typing import Callable

from doc_viewer.domain.models.category.recents_smart_category import RecentsSmartCategory
import doc_viewer.settings.config as config
from doc_viewer.domain.models.category.category import Category
from .normal_category import NormalCategory
from .smart_category import SmartCategory

from doc_viewer.domain.models.document.document import Document
from .predicates import (
    is_favourited
)

from doc_viewer.domain.events.event_bus import event_bus
from doc_viewer.domain.events.event import Event
from doc_viewer.domain.events.document.document_events import(
    DocumentEvent,
    DocumentAddedEvent,
    DocumentRemovedEvent,
    DocumentFavouritedEvent,
)

logger = logging.getLogger(__name__)  

class CategoryController:
    def __init__(self):
        self._categories = {}
        self.setup_smart_categories()
        self.subscribe_events()

    def setup_smart_categories(self):
        """Setup initial smart categories."""

        self.add_smart_category(
            name=config.FAVOURITES_CATEGORY_NAME,
            predicate=is_favourited
        )

        self.add_smart_category(
            name=config.RECENTS_CATEGORY_NAME,
        )

    def subscribe_events(self):
        """Subscribe to relevant events."""
        # Document favourited event
        event_bus.subscribe(DocumentEvent, self.handle_event)

    def handle_event(self, event: Event):
        """Handle events."""

        # Document favourited event
        if isinstance(event, DocumentFavouritedEvent):
            document = event.get_document()
            if document.is_favourited():
                self.add_document("Favourites", document)
            else:
                self.remove_document("Favourites", document)
            self.get_category("Recents").sort_documents()
        # Document added event
        elif isinstance(event, DocumentAddedEvent):
            document = event.get_document()
            self.add_document("Recents", document)
        elif isinstance(event, DocumentRemovedEvent):
            document = event.get_document()
            self.remove_document_all_categories(document)

    def add_smart_category(
            self,
            name: str, 
            predicate: Callable[[Document], bool]= lambda doc: True
    ) -> bool:
        """
        Adds a smart category.

        Args:
            name (str): The name of the smart category.
            predicate (Callable[[Document], bool]): A function that takes a document 
            and returns True if it belongs to the category.

        Returns:
            bool: True if the category was added successfully, False otherwise.
        """
        if name == config.RECENTS_CATEGORY_NAME:
            smart_category = RecentsSmartCategory(name)
        else:
            smart_category = SmartCategory(name, predicate)

        if smart_category:
            logger.debug(f"Adding smart category: {name}")
            self._categories[name] = smart_category
            return True
        return False

    def add_normal_category(self, name: str) -> bool:
        """
        Adds a normal category.

        Args:
            name (str): The name of the normal category.

        Returns:
            bool: True if the category was added successfully, False otherwise.
        """
        normal_category = NormalCategory(name)
        if normal_category:
            logger.debug(f"Adding normal category: {name}")
            self._categories[name] = normal_category
            return True
        return False

    def remove_category(self, name: str) -> bool:
        """
        Removes a category by name.

        Args:
            name (str): The name of the category to remove.

        Returns:
            bool: True if the category was removed successfully, False otherwise.
        """
        if name in self._categories:
            logger.debug(f"Removing category: {name}")
            del self._categories[name]
            return True
        return False

    def get_categories(self):
        """
        Returns a list of all categories.
        """
        return self._categories
    
    def get_category(self, name: str) -> Category | None:
        """
        Returns a category by name.

        Args:
            name (str): The name of the category.

        Returns:
            Category | None: The category if found, None otherwise.
        """
        return self._categories.get(name)

    def add_document(self, category_name: str, document: Document) -> bool:
        """
        Adds a document to a category.

        Args:
            category_name (str): The name of the category.
            document (Document): The document to add.

        Returns:
            bool: True if the document was added successfully, False otherwise.
        """
        if category_name in self._categories:
            logger.debug(f"Adding document to category: {category_name}")
            self._categories[category_name].add_document(document)
            return True
        return False

    def remove_document(self, category_name: str, document: Document) -> bool:
        """
        Removes a document from a category.

        Args:
            category_name (str): The name of the category.
            document (Document): The document to remove.

        Returns:
            bool: True if the document was removed successfully, False otherwise.
        """
        if category_name in self._categories:
            logger.debug(f"Removing document from category: {category_name}")
            self._categories[category_name].remove_document(document)
            return True
        return False
    
    def remove_document_all_categories(self, document: Document):
        """
        Removes a document from all categories.

        Args:
            document (Document): The document to remove.
        """
        logger.debug("Removing document from all categories...")
        for category in self._categories.keys():
            self.remove_document(category, document)
