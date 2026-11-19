
from tools import analyze_resume_pdf
from report_generator import save_analysis


def main():

    print("================================")
    print("       AI RESUME ANALYZER")
    print("================================")

    pdf_path = input("Enter resume PDF path: ")

    try:

        print("\nAnalyzing your resume with AI...\n")

        # Generate AI resume analysis
        result = analyze_resume_pdf(pdf_path)

        print("========== RESUME ANALYSIS ==========\n")
        print(result)

        # Save AI analysis into text file
        report_path = save_analysis(result)

        print("\n=====================================")
        print("Analysis completed successfully!")
        print("Report saved at:", report_path)
        print("=====================================")

    except Exception as e:

        print("Error:", e)


if __name__ == "__main__":
    main()
