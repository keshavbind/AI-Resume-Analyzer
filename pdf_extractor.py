
import os
from pypdf import PdfReader
from pypdf.errors import PdfReadError


def extract_resume_text(pdf_path):

    # 1. Check whether file exists
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError("PDF file not found!")

    # 2. Check file extension
    if not pdf_path.lower().endswith(".pdf"):
        raise ValueError("Please provide a PDF file!")

    # 3. Open and read PDF
    try:

        reader = PdfReader(pdf_path)

        resume_text = ""

        for page in reader.pages:

            text = page.extract_text()

            if text:
                resume_text += text + "\n"

    except PdfReadError:
        raise ValueError("Invalid or corrupted PDF file!")

    except OSError:
        raise OSError("Unable to access or read the PDF file!")

    # 4. Check extracted text
    if not resume_text.strip():
        raise ValueError(
            "No readable text found! This PDF may be scanned."
        )

    return resume_text


# Test PDF extraction
if __name__ == "__main__":

    pdf_path = "missing.pdf"

    try:

        text = extract_resume_text(pdf_path)

        print("Resume Text:")
        print(text)

    except (FileNotFoundError, ValueError, OSError) as e:

        print("Error:", e)
