
import os
from datetime import datetime


def save_analysis(analysis):

    # Create output folder if it doesn't exist
    os.makedirs("output", exist_ok=True)

    # Generate current timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Generate unique report filename
    file_name = f"resume_analysis_{timestamp}.txt"

    # Create complete file path
    file_path = os.path.join("output", file_name)

    # Save analysis
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(analysis)

    return file_path


if __name__ == "__main__":

    path = save_analysis("This is my first AI resume report.")

    print("Report saved successfully!")
    print("File location:", path)
