class UIDocument:
    def __init__(self, file_path: str):
        self._file_path = file_path

    def get_file_path(self) -> str:
        return self._file_path