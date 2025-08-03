from abc import ABC, abstractmethod

class Document(ABC):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.pages = []
        self.num_pages = 0
        self.extension = ""
        self.doc = None
        self.load_document()

    @abstractmethod
    def load_document(self):
        pass

