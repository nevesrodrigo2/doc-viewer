# PySide6 Imports
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout, QLabel,
    QPushButton, QScrollArea, QStackedWidget, QSizePolicy
)
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtPdf import QPdfDocument
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt, QSize
# Project Imports
from doc_viewer.ui.components.document_viewer.thumbnail_catalog import thumbnail_catalog
from doc_viewer.ui.components.document_viewer.thumbnail import Thumbnail

import logging
logger = logging.getLogger(__name__)

class ThumbnailPanel(QWidget):
    """
    Panel to manage multiple thumbnail viewers.
    """
    def __init__(self):
        super().__init__()
        self._thumbnail_viewers = []

        # Create a scrollable area
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        layout = QVBoxLayout(self)
        layout.addWidget(scroll)

        # Container inside the scroll area
        self.container = QWidget()

        self.grid_layout = QGridLayout(self.container)
        self.grid_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        scroll.setWidget(self.container)

        # Keep track of grid positions
        self._row = 0
        self._col = 0
        self._max_columns = 4  

    def add_thumbnail_viewer(self, document):  
        """
        Add a thumbnail viewer to the panel.

        Args:
            document (QPdfDocument): The PDF document to create a thumbnail for.
        """

        doc_path = document.get_file_path()
        thumbnails_catalog = thumbnail_catalog.get_thumbnails()

        # Check if thumbnail already exists
        if doc_path in thumbnails_catalog.keys():
            thumbnail_pixmap = thumbnails_catalog[doc_path]
            logger.debug(f"Thumbnail pixmap already exists for {doc_path}, reusing it.")
        else:
            thumbnail_pixmap = self.make_thumbnail(document)
            if thumbnail_pixmap:
                # Store in catalog
                thumbnail_catalog.add_thumbnail(doc_path, thumbnail_pixmap)
                logger.debug(f"Created new thumbnail for {doc_path}.")

        if thumbnail_pixmap:
            # Add to grid layout
            thumbnail_widget = Thumbnail(doc_path, thumbnail_pixmap)
            self.grid_layout.addWidget(thumbnail_widget, self._row, self._col)

            # Update row/column for next thumbnail
            self._col += 1
            if self._col >= self._max_columns:
                self._col = 0
                self._row += 1

            # Keep track of thumbnails
            self._thumbnail_viewers.append(thumbnail_widget)

    def make_thumbnail(self, doc) -> QPixmap:
        """
        Render first page of PDF as a thumbnail pixmap.
        Args:
            doc (PdfDocument): The PDF document to render.

        Returns:
            QPixmap: The rendered thumbnail pixmap.
        """
        logger.debug("Rendering thumbnail...")

        if doc.pageCount() > 0:
            image = doc.render(0, QSize(150, 200))  # first page
            thumbnail_pixmap = QPixmap.fromImage(image)
            # Create Thumbnail widget (or QLabel if simple)
        return thumbnail_pixmap

    def remove_thumbnail_viewer(self, file_path: str):
        """
        Remove a thumbnail viewer from the panel.

        Args:
            file_path (str): The file path of the document whose thumbnail to remove.
        """
        thumbnails = self.get_thumbnail_viewers()
        for thumb in thumbnails:
            if thumb.get_document_path() == file_path:
                self.grid_layout.removeWidget(thumb)
                thumb.deleteLater()
                self._thumbnail_viewers.remove(thumb)
                logger.debug(f"Removed thumbnail for {file_path}")
                break
    
    def remove_thumbnail(self, file_path: str):
        """
        Remove a thumbnail from the catalog.

        Args:
            file_path (str): The file path of the document whose thumbnail to remove.
        """
        thumbnail_catalog.remove_thumbnail(file_path)
        logger.debug(f"Removed thumbnail from catalog for {file_path}")

    def get_thumbnail_viewers(self):
        """
        Get the list of thumbnail viewers in the panel.

        Returns:
            list[Thumbnail]: The list of thumbnail viewers.
        """
        return self._thumbnail_viewers
    
    def __str__(self):
        return (
            f"<ThumbnailPanel with {len(self._thumbnail_viewers)} thumbnails>"
            f" viewers: {self._thumbnail_viewers}"
        )