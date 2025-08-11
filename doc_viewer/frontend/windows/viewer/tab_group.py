from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QSpacerItem, QLabel, QScrollArea
from PySide6.QtCore import Qt
class TabGroup(QWidget):
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
        # Insert labels ABOVE the spacer
        index_before_spacer = self.layout.count() - 1
        for doc in self.documents:
            doc_name = doc.rsplit('/', 1)[-1]
            if doc_name not in self.doc_names:
                self.doc_names.append(doc_name)
                label = QLabel(doc_name)
                label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                self.layout.insertWidget(index_before_spacer, label)