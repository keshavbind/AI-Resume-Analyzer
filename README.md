# AI Resume Analyzer

An AI-powered Resume Analyzer built using Python and Google's Gemini API. It extracts text from PDF resumes, analyzes candidate information using Generative AI, and generates a structured resume feedback report.

## Features

- **PDF Text Extraction:** Extracts text from PDF resumes using PyPDF.
- **PDF Validation:** Handles missing, invalid, corrupted, and scanned PDFs.
- **AI Resume Analysis:** Uses Google's Gemini API to analyze resume content.
- **Resume Feedback:** Identifies technical skills, soft skills, education, experience, strengths, weaknesses, and improvement suggestions.
- **Report Generation:** Saves analysis results as timestamped text files.
- **Error Handling:** Handles common file and PDF errors.

## Technologies Used

- Python
- Google Gemini API
- Google GenAI SDK
- PyPDF
- Python-dotenv

## Project Structure

```text
AI-Resume-Analyzer/
│
├── main.py
├── pdf_extractor.py
├── resume_analyzer.py
├── report_generator.py
├── tools.py
├── requirements.txt
├── .env
├── .gitignore
│
└── output/
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/keshavbind/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

### 2. Install dependencies

```bash
py -3.14 -m pip install -r requirements.txt
```

### 3. Configure Gemini API

Create a `.env` file in the project directory:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder with your own Gemini API key.

### 4. Run the application

```bash
py -3.14 main.py
```

Enter the path of your PDF resume when prompted.

## How It Works

1. The user provides a PDF resume.
2. Python extracts readable text from the PDF.
3. The extracted text is sent to Google's Gemini API.
4. Gemini analyzes the resume and generates structured feedback.
5. The application displays the analysis.
6. The report is saved inside the `output` folder.

## Future Improvements

- OCR support for scanned PDF resumes.
- Resume scoring system.
- Job description matching.
- Keyword and ATS analysis.
- PDF report generation.
- Web-based user interface.

## Security

- Never upload your `.env` file or API key.
- Do not upload personal resumes without permission.
- Generated reports are excluded from version control.

## Author

**Keshav Bind**

B.Sc. Information Technology Graduate | Android Developer | AI Developer (Learning)