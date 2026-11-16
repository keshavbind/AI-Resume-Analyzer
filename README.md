# AI Resume Analyzer

An AI-powered Resume Analyzer built using Python, Streamlit, and Google Gemini API. Upload your resume in PDF format and receive AI-generated feedback about your technical skills, education, experience, strengths, weaknesses, and improvement suggestions.

## Features

- **PDF Resume Upload:** Upload resumes directly through a web interface.
- **PDF Text Extraction:** Extract readable text from PDF documents using pypdf.
- **AI Resume Analysis:** Analyze resumes using Google Gemini API.
- **Technical Skills Analysis:** Identify programming languages, frameworks, and tools.
- **Resume Feedback:** Identify strengths, weaknesses, and improvement opportunities.
- **Report Download:** Download the generated analysis as a text file.
- **Command-Line Support:** Run the analyzer through the terminal as well.

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- Google GenAI SDK
- pypdf
- python-dotenv

## Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── main.py
├── pdf_extractor.py
├── resume_analyzer.py
├── report_generator.py
├── tools.py
│
├── requirements.txt
├── README.md
├── .gitignore
│
└── output/
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/keshavbind/AI-Resume-Analyzer.git
```

### 2. Navigate to the project directory

```bash
cd AI-Resume-Analyzer
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini API Key

Create a `.env` file in the project directory:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Get your API key from Google AI Studio.

### 5. Run the Streamlit Web Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal.

## Run the Command-Line Application

You can also use the original command-line version:

```bash
python main.py
```

Enter the path to your resume PDF when prompted.

## How It Works

1. Upload a PDF resume or provide its path through the command line.
2. Extract resume text using pypdf.
3. Send the extracted text to Google Gemini.
4. Generate structured AI feedback.
5. Display the analysis or save and download the report.

## Future Improvements

- ATS compatibility scoring
- Job description matching
- Keyword analysis
- Professional PDF report generation
- Improved dashboard and visualizations
- OCR support for scanned resumes

## Security

- Keep your Gemini API key inside `.env`.
- Never upload `.env` or personal resume files to GitHub.
- Do not share resumes without the owner's permission.

## Author

**Keshav Bind**

GitHub: https://github.com/keshavbind