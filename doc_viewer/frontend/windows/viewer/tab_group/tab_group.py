from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QSpacerItem, QLabel, QScrollArea
from PySide6.QtCore import Qt, Signal

from doc_viewer.frontend.windows.viewer.tab_group.tab.tab import Tab
from doc_viewer.frontend.events.event_bus import event_bus


class TabGroup(QWidget):

    """A widget that manages a group of tabs for recently edited documents."""
    def __init__(self):
        super().__init__()
        self.document_paths = []
        self.doc_names = []

        # make the tab group scrollable
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)  
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  

        # setup layout for the tab group
        self.container = QWidget()
        self.layout = QVBoxLayout(self.container)

        # Add the spacer *once*
        self.layout.addSpacerItem(QSpacerItem(
            0, 0,
            QSizePolicy.Minimum,
            QSizePolicy.Expanding
        ))
        
        scroll_area.setWidget(self.container)

        outer_layout = QVBoxLayout(self)
        outer_layout.addWidget(scroll_area)

    def load_document(self, document_path):
        """Load document names into the tab group."""
        # Insert labels ABOVE the spacer
        index_before_spacer = self.layout.count() - 1
        doc_name = document_path.rsplit('/', 1)[-1]
        if doc_name not in self.doc_names:
            self.doc_names.append(doc_name)
            tab = Tab(doc_name)
            # label = QLabel(doc_name)
            # label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            self.layout.insertWidget(index_before_spacer, tab)
    
    def change_document(self, index):
        """Change the currently displayed document by index."""
        if 0 <= index < len(self.doc_names):
            print(f"Changing to document: {self.doc_names[index]}")
        else:
            raise IndexError("Index out of range for tab group.")
        
    def mousePressEvent(self, event):
        tab = self.childAt(event.pos())
        if isinstance(tab, Tab):
            event_bus.emit('document_changed', tab.get_doc_name())
        return super().mousePressEvent(event)