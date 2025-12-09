import io
from typing import Union

from PyPDF2 import PdfReader


def extract_text_from_pdf(file: Union[str, bytes, io.BytesIO]) -> str:
    """
    Extract text from a PDF.

    Parameters
    ----------
    file : str | bytes | io.BytesIO
        - If str: treated as a file path.
        - If bytes or BytesIO: raw file content (e.g. from Streamlit upload).

    Returns
    -------
    str
        Extracted text from all pages of the PDF.
    """
    # Handle file path vs file-like object
    if isinstance(file, str):
        # file is a path
        reader = PdfReader(file)
    else:
        # file is bytes or BytesIO (e.g., Streamlit's UploadedFile)
        if isinstance(file, bytes):
            file = io.BytesIO(file)
        reader = PdfReader(file)

    all_text = []
    for page in reader.pages:
        page_text = page.extract_text() or ""
        all_text.append(page_text)

    raw_text = "\n".join(all_text)
    cleaned_text = _clean_whitespace(raw_text)
    return cleaned_text


def _clean_whitespace(text: str) -> str:
    """
    Normalize whitespace in extracted text:
    - Strip extra spaces
    - Collapse multiple newlines
    """
    # Replace Windows newlines etc.
    text = text.replace("\r", "\n")
    # Collapse multiple newlines
    lines = [line.strip() for line in text.split("\n")]
    # Keep only non-empty lines
    lines = [line for line in lines if line]
    return "\n".join(lines)
