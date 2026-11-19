from pydantic import BaseModel
from fastapi import FastAPI, UploadFile, File, HTTPException
from tools import analyze_resume_pdf
import traceback


app = FastAPI(
    title="AI Resume Analyzer API",
    description="Backend for AI-powered resume analysis",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "AI Resume Analyzer API is running!",
        "status": "success"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "AI Resume Analyzer",
        "version": "1.0.0"
    }



class UserRequest(BaseModel):
    name: str
    role: str

@app.post("/test")
def test_post(data: UserRequest):
    return {
        "message": "POST request received successfully!",
        "name": data.name,
        "role": data.role
    }



@app.post("/analyze")
async def analyze_resume(file: UploadFile = File(...)):

    try:
        # 1. Check filename
        if not file.filename or not file.filename.lower().endswith(".pdf"):
            raise HTTPException(
                status_code=400,
                detail="Please upload a PDF file!"
            )

        # 2. Read uploaded file
        content = await file.read()

        # 3. Check empty file
        if not content:
            raise HTTPException(
                status_code=400,
                detail="Uploaded PDF is empty!"
            )

        # 4. Check PDF signature
        if not content.startswith(b"%PDF-"):
            raise HTTPException(
                status_code=400,
                detail="Invalid PDF file!"
            )

        # Reset file position before extraction
        await file.seek(0)

        # 5. Analyze resume
        result = analyze_resume_pdf(file.file)

        return {
            "status": "success",
            "message": "Resume analyzed successfully!",
            "filename": file.filename,
            "analysis": result
        }

    except HTTPException:
        raise

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception as e:
        print("ACTUAL ERROR:", repr(e))
        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail="Resume analysis failed. Please try again."
        )

    finally:
        await file.close()

