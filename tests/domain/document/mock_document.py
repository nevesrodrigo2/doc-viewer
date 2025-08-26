from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_mock_pdf(temp_dir: Path, filename="mock.pdf", title="Test PDF", author="Unit Test Author", content="Hello World"):
    path = temp_dir / filename
    c = canvas.Canvas(str(path), pagesize=letter)
    c.setTitle(title)
    c.setAuthor(author)
    
    # Set font (important for PyMuPDF text extraction)
    c.setFont("Helvetica", 12)
    
    # Draw the content
    c.drawString(100, 750, content)
    
    c.showPage()
    c.save()
    return str(path)



def create_empty_pdf(temp_dir: Path, filename="empty.pdf"):
    """
    Minimal empty PDF with no metadata or content, saved to temp directory.
    """
    path = temp_dir / filename
    c = canvas.Canvas(str(path))
    c.showPage()
    c.save()
    return str(path)


def create_multi_page_pdf(temp_dir: Path, filename="multi.pdf", num_pages=3, title=None, author=None, content="Page"):
    """
    PDF with multiple pages, optional metadata, saved to temp directory.
    """
    path = temp_dir / filename
    c = canvas.Canvas(str(path))
    if title:
        c.setTitle(title)
    if author:
        c.setAuthor(author)

    for i in range(1, num_pages + 1):
        c.drawString(100, 750, f"{content} {i}")
        c.showPage()
    c.save()
    return str(path)
