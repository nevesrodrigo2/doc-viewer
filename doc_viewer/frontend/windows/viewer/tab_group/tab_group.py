from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QSpacerItem, QLabel, QScrollArea
from PySide6.QtCore import Qt, Signal

from doc_viewer.frontend.windows.viewer.tab_group.tab.tab import Tab


class TabGroup(QWidget):
    document_changed = Signal(str)

    """A widget that manages a group of tabs for recently edited documents."""
    def __init__(self, documents):
        super().__init__()
        self.documents = documents
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

    def load_documents(self):
        """Load document names into the tab group."""
        # Insert labels ABOVE the spacer
        index_before_spacer = self.layout.count() - 1
        for doc in self.documents:
            doc_name = doc.rsplit('/', 1)[-1]
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
            self.document_changed.emit(tab.get_doc_name())
        return super().mousePressEvent(event)