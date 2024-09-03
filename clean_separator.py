import sys
import re
import os
import glob

def find_hust_chatbot_lines(file_path):
    """
    Finds line numbers in a markdown file where a line ends with roman numerals
    (I. to V), single-digit numbers (1. to 9.), uppercase letters (A. to E), or
    lowercase letters (a. to e) followed by a period (with a space before lowercase letters).
    Excludes lines ending with multi-digit numbers (e.g., 2023.) unless the number is at the start of the line.
    The next line must be '---HUST_CHATBOT---'. Moves the recognized part to the start of the line + 2

    Args:
        file_path: Path to the markdown file.

    Returns:
        None (modifies the file directly).
    """

    with open(file_path, 'r', encoding="utf-8") as file:
        lines = file.readlines()

    with open(file_path, 'w', encoding="utf-8") as file:
        for i in range(len(lines) - 2):  # Iterate until the second-to-last line
            match = re.search(
                r"(^[1-9]\.$|(?:\b[IVX]{1,3}\.|10\.|[A-E]\.|\s[a-e]\.|\s[1-9]\.))$",
                lines[i].rstrip()
            )
            if match and lines[i + 1].strip() == '---HUST_CHATBOT---':
                # Move the matched digit/number two lines down
                extracted_part = match.group(0) 
                lines[i] = lines[i].rstrip()[:-len(extracted_part)] + "\n"
                lines[i + 2] = extracted_part + " " + lines[i + 2].lstrip()

        file.writelines(lines)

def process_markdown_files(folder_path):
    """
    Processes all markdown files in the given folder.

    Args:
        folder_path: Path to the folder containing markdown files.
    """

    markdown_files = glob.glob(os.path.join(folder_path, '*.md'))

    for md_file in markdown_files:
        find_hust_chatbot_lines(md_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python find_lines.py <my_folder>")
        sys.exit(1)

    folder_path = sys.argv[1]

    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        sys.exit(1)

    process_markdown_files(folder_path)

    print("Markdown files processed.") 