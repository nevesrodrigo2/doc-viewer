class UIDocument:
    """
    A class representing a document in the UI.
    """
    def __init__(self, file_path: str):
        self._file_path = file_path
        self._is_favourited = False

    def get_file_path(self) -> str:
        return self._file_path

    def is_favourited(self) -> bool:
        return self._is_favourited

    def set_favourited(self, favourited: bool):
        self._is_favourited = favourited