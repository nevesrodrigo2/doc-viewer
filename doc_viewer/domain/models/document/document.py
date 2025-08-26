import datetime

class Document:
    """Class representing a document."""
    def __init__(self, doc, path: str):
        self._doc = doc
        self._path = path
        self.set_metadata()
        self.set_content()
        self._is_favourited = False
        self.last_interacted_at = datetime.datetime.now() 

    def set_metadata(self):
        """Set document metadata."""
        self._metadata = {
            "path": self._path,
            "page_count": self._doc.page_count,
            "title": self._doc.metadata.get("title", ""),
            "author": self._doc.metadata.get("author", ""),
        }

    def get_metadata(self):
        """Get document metadata."""
        return self._metadata
    
    def set_favourite(self, is_favourited: bool):
        """Set the document as favourited or not."""
        self._is_favourited = is_favourited

    def is_favourited(self) -> bool:
        """Check if the document is favourited."""
        return self._is_favourited

    def get_file_path(self) -> str:
        """Get the file path of the document."""
        return self._metadata.get("path", "")

    def get_page_count(self) -> int:
        """Get the number of pages in the document."""
        return self._metadata.get("page_count", 0)

    def get_title(self) -> str:
        """Get the title of the document."""
        return self._metadata.get("title", "")

    def get_author(self) -> str:
        """Get the author of the document."""
        return self._metadata.get("author", "")

    def set_content(self):
        """
        Sets the content of the document by extracting text from each page.
        """
        self._content = ""
        for page in self._doc:
            self._content += page.get_text("text")
    
    def get_content(self) -> str:
        """Get the content of the document."""
        return self._content

    def set_last_interacted_at(self, timestamp= datetime.datetime.now()):
        """Set the last interacted at timestamp of the document."""
        self.last_interacted_at = timestamp

    def get_last_interacted_at(self) -> datetime.datetime:
        """Get the last interacted at timestamp of the document."""
        return self.last_interacted_at