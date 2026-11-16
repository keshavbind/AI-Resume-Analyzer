
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

# Initialize Gemini
client = genai.Client(api_key=api_key)


def analyze_resume(resume_text):

        if not resume_text or not resume_text.strip():
             raise ValueError("Resume text is empty!")


        prompt = f"""
        You are an expert AI Resume Analyzer.

        Analyze the following resume carefully.

        RESUME:
        {resume_text}

        Provide your analysis in the following sections:

        1. Technical Skills
        2. Soft Skills
        3. Education
        4. Experience
        5. Resume Strengths
        6. Weaknesses
        7. Improvement Suggestions
        8. Overall Resume Feedback

        Give clear, practical and honest feedback.
        Do not invent qualifications or experience.

        IMPORTANT RULES:

        - Never invent skills, experience, certifications or achievements.
        - Do not suggest fake project metrics.
        - Clearly distinguish confirmed information from assumptions.
        - Do not assume the candidate is still a student if graduation is complete.
        - Give recommendations suitable for an entry-level candidate.
        - Do not treat missing information as proof of lack of ability.
        - Treat the current date as November 2026.
        - If the resume lists a graduation year of 2026,
        treat the degree as completed unless the resume
        explicitly says otherwise.
        - Do not describe a completed graduate as a current student.
        """

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        return response.text

if __name__ == "__main__":

    from pdf_extractor import extract_resume_text

    # Extract resume text
    resume_text = extract_resume_text("resume.pdf")

    print("\nAnalyzing resume with Gemini...\n")

    # Analyze resume
    result = analyze_resume(resume_text)

    print("===== AI RESUME ANALYSIS =====")
    print(result)