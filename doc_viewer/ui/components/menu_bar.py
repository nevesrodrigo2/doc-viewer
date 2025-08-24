from PySide6.QtWidgets import QMenuBar

class MenuBar(QMenuBar):
    """Menu bar for the application."""
    def __init__(self):
        super().__init__()
        self.setup_bar()

    def setup_bar(self):
        """Setup the menu bar with predefined menus and actions."""
        menus = [
            ("File", ["Open", "Save", "Exit"]),
            ("Edit", ["Undo", "Redo", "Copy", "Paste"]),
            ("View", ["Zoom In", "Zoom Out"]),
            ("Help", ["About", "Keyboard Shortcuts"])
        ]

        for menu_name, actions in menus:
            menu = self.addMenu(menu_name)
            for action in actions:
                menu.addAction(action)
