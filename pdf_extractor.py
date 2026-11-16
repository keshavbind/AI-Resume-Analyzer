
import os
from pypdf import PdfReader
from pypdf.errors import PdfReadError


def extract_resume_text(pdf_source):

    # Check whether source is a file path or uploaded file
    if isinstance(pdf_source, (str, os.PathLike)):

        pdf_path = os.fspath(pdf_source)

        if not os.path.isfile(pdf_path):
            raise FileNotFoundError("PDF file not found!")

        if not pdf_path.lower().endswith(".pdf"):
            raise ValueError("Please provide a PDF file!")

    else:
        # Handle uploaded PDF files
        filename = getattr(pdf_source, "name", "")

        if not filename.lower().endswith(".pdf"):
            raise ValueError("Please provide a PDF file!")

        if not hasattr(pdf_source, "read"):
            raise ValueError("Invalid uploaded file!")

        pdf_source.seek(0)

    # Extract PDF text
    try:

        reader = PdfReader(pdf_source)

        resume_text = ""

        for page in reader.pages:

            text = page.extract_text()

            if text:
                resume_text += text + "\n"

    except PdfReadError:
        raise ValueError("Invalid or corrupted PDF file!")

    except OSError:
        raise OSError("Unable to access or read the PDF file!")

    # Check extracted text
    if not resume_text.strip():
        raise ValueError(
            "No readable text found! This PDF may be scanned."
        )

    return resume_text


# Test PDF extraction
if __name__ == "__main__":

    try:
        text = extract_resume_text("resume.pdf")

        print("Resume Text:")
        print(text)

    except (FileNotFoundError, ValueError, OSError) as e:
        print("Error:", e)
