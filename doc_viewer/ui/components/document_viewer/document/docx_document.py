# Project Imports
from .document import UIDocument

class DOCXDocument(UIDocument):
    def __init__(self, file_path: str):
        super().__init__(file_path)