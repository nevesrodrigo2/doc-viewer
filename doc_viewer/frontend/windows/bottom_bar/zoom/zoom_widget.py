from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide6.QtCore import Qt, Signal

from doc_viewer.frontend.windows.bottom_bar.zoom.zoom_slider import ZoomSlider
from doc_viewer.frontend.events.event_bus import event_bus

class ZoomWidget(QWidget):
    """A widget for zooming in and out of the document viewer."""
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)
        self.zoom_slider = ZoomSlider(self)

        self.layout.addWidget(self.zoom_slider)
        self.layout.setSpacing(20) # space between slider and label

        self.zoom_slider_value = self.zoom_slider.get_slider_value()
        self.label = QLabel(f"{self.zoom_slider_value}%")
        
        self.layout.addWidget(self.label)
        event_bus.subscribe('zoom_level_changed', self.update_zoom_label)
            
    def update_zoom_label(self, value: int):
        """Update the zoom level label."""
        print(f"Zoom level changed to: {value}%")
        self.label.setText(f"{value}%")