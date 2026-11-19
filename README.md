# AI Resume Analyzer

An AI-powered Resume Analyzer built using Python, Google Gemini API, FastAPI, and Streamlit. Upload your resume in PDF format and receive AI-generated feedback about your skills, education, experience, strengths, weaknesses, and improvement suggestions.

## Features

- **PDF Resume Upload:** Upload resumes through a web interface.
- **PDF Text Extraction:** Extract readable text from PDF documents using pypdf.
- **AI Resume Analysis:** Analyze resumes using Google Gemini API.
- **Technical Skills Analysis:** Identify programming languages, frameworks, and tools.
- **Experience Analysis:** Review professional experience and career history.
- **Resume Feedback:** Identify strengths, weaknesses, and improvement opportunities.
- **Report Download:** Download the generated analysis as a text file.
- **FastAPI Backend:** Process resume uploads and return AI-generated analysis through REST API endpoints.
- **Command-Line Support:** Run the analyzer through the terminal.

## Tech Stack

- Python
- Google Gemini API
- Google GenAI SDK
- FastAPI
- Uvicorn
- Streamlit
- Requests
- pypdf
- python-dotenv

## Project Architecture

The application follows a frontend-backend architecture:

1. Streamlit provides the user interface.
2. The user uploads a PDF resume.
3. Streamlit sends the PDF to the FastAPI backend.
4. FastAPI extracts resume text and sends it for AI analysis.
5. Google Gemini generates the analysis.
6. FastAPI returns the result to Streamlit.
7. Streamlit displays the analysis and provides a download option.

## Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py                 # Streamlit frontend
├── main.py                # FastAPI backend
├── cli_main.py            # Command-line application
├── tools.py               # Resume analysis workflow
├── pdf_extractor.py       # PDF text extraction
├── resume_analyzer.py     # Gemini AI analysis
├── report_generator.py    # Analysis report generation
│
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
├── .gitignore             # Ignored files
│
└── .env                   # Gemini API key (create locally)
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

Get your API key from [Google AI Studio](https://aistudio.google.com/).

Keep your API key private. Never commit your `.env` file to GitHub.

## Running the Application

The application requires two running processes.

### 1. Start the FastAPI Backend

Open a terminal and run:

```bash
uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

FastAPI Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

### 2. Start the Streamlit Frontend

Open a second terminal and run:

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to use the application.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| GET | `/health` | Health check |
| POST | `/test` | Test the API with JSON input |
| POST | `/analyze` | Upload and analyze a PDF resume |

### Resume Analysis API

- **Endpoint:** `/analyze`
- **Method:** `POST`
- **Input:** PDF file upload
- **Output:** AI-generated resume analysis

You can test the endpoints using the FastAPI Swagger interface at `/docs`.

## Run the Command-Line Application

You can also use the command-line version:

```bash
python cli_main.py
```

Enter the path to your resume PDF when prompted.

## How It Works

1. Upload a PDF resume through Streamlit or provide its path through the command line.
2. Extract resume text using pypdf.
3. Send the extracted text to Google Gemini.
4. Generate structured AI feedback.
5. Display the analysis and provide a downloadable report.

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
- Generated reports and personal documents should remain private.
- Do not share resumes without the owner's permission.

## Author

**Keshav Bind**

GitHub: https://github.com/keshavbind