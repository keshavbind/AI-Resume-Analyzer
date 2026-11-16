
from pdf_extractor import extract_resume_text
from resume_analyzer import analyze_resume


def analyze_resume_pdf(pdf_path):

    # Extract text from PDF
    resume_text = extract_resume_text(pdf_path)

    if not resume_text.strip():
        raise ValueError("No readable text found in resume PDF!")

    # Send extracted text to Gemini
    analysis = analyze_resume(resume_text)

    return analysis
