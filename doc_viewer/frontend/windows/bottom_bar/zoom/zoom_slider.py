from PySide6.QtWidgets import QSlider
from PySide6.QtCore import Qt, Signal

from doc_viewer.frontend.events.event_bus import event_bus


class ZoomSlider(QSlider):
    """A slider widget for zooming in and out of documents."""
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setOrientation(Qt.Horizontal)
        self.setMinimum(50)
        self.setMaximum(150)
        self.setSingleStep(10)

        # Default zoom level at 100%
        self.setValue(100)  
        self.setTickInterval(10)
        self.setTickPosition(QSlider.TicksBelow)

        # set signals
        self.set_signals()

    def get_slider_value(self):
        """Return the current value of the zoom slider."""
        return self.value()

    def set_slider_value(self, value: int):
        """Set the value of the zoom slider."""
        if self.minimum() <= value <= self.maximum():
            self.setValue(value)
        else:
            raise ValueError(f"Value {value} is out of range ({self.minimum()}-{self.maximum()})")
    
    def set_signals(self):
        """Connect the slider's valueChanged signal to a custom slot."""
        self.valueChanged.connect(self.on_value_changed)

    def on_value_changed(self, value: int):
        """Override to handle value changes."""
        # emit signal for zoom level change
        self.emit_event('zoom_level_changed', value)

    def emit_event(self, event_name, *args, **kwargs):
        """emit an event to the event bus."""
        event_bus.emit(event_name, *args, **kwargs)
        print(f"Event '{event_name}' published with args: {args} and kwargs: {kwargs}")
    