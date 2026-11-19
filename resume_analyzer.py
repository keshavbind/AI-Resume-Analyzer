
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
    You are an expert AI Resume Analyzer and Career Advisor.

    Analyze the following resume carefully and provide
    accurate, detailed and practical feedback.

    RESUME:
    {resume_text}

    Provide your analysis in the following sections:

    1. Technical Skills
       - Identify programming languages, frameworks,
         databases, tools and technologies.
       - Group skills into relevant categories.
       - Do not add skills that are not mentioned.

    2. Soft Skills
       - Identify soft skills supported by resume evidence.
       - Explain briefly which responsibility or activity
         demonstrates each skill.
       - Do not assume a soft skill without evidence.

    3. Education
       - Identify degree, institution and graduation year.
       - Distinguish completed education from ongoing education.
       - Do not assume missing qualifications.

    4. Experience
       - Identify every professional role, company and duration.
       - Calculate experience in each role when dates are available.
       - Calculate total professional experience separately.
       - Distinguish current-role experience from total experience.
       - Do not count overlapping employment periods twice.
       - Consider employment gaps where dates allow.
       - If dates are incomplete or unclear, explain the limitation.
       - Use November 19, 2026 as the current date.

    5. Resume Strengths
       - Highlight relevant skills, experience, projects
         and career progression.
       - Support observations using resume information.

    6. Weaknesses
       - Identify missing details, unclear descriptions
         and areas that could be improved.
       - Do not treat missing information as proof
         that the candidate lacks a particular ability.

    7. Improvement Suggestions
       - Give specific and actionable recommendations.
       - Suggest adding measurable achievements only
         when the candidate can verify them.
       - Recommend relevant technical or professional skills
         based on the candidate's experience level.

    8. Overall Resume Feedback
       - Summarize the candidate's profile.
       - Identify suitable job roles based on the resume.
       - Give an honest assessment of resume quality.
       - Mention the most important improvements.

    IMPORTANT ANALYSIS RULES:

    - Never invent skills, experience, certifications,
      achievements or qualifications.
    - Never create fake project metrics or company details.
    - Distinguish information stated in the resume
      from assumptions or inferred observations.
    - Use phrases such as "The resume states" rather than
      claiming information has been independently verified.
    - Calculate total experience using all employment periods.
    - Do not count overlapping employment periods twice.
    - Do not confuse current-role experience with total experience.
    - If employment dates are missing, do not guess durations.
    - Consider the candidate's actual career stage:
      fresher, entry-level, experienced or senior.
    - Do not automatically treat every candidate as a fresher.
    - Do not assume the candidate is still a student
      if graduation is complete.
    - Treat a 2026 graduation as completed unless
      the resume explicitly states otherwise.
    - Do not assume the candidate is currently employed
      unless the resume indicates it.
    - Give clear, honest and practical feedback.

    Return the analysis in a professional and readable format.
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
