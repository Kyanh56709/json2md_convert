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
    The next line must be '---HUST_CHATBOT---'.

    Args:
        file_path: Path to the markdown file.

    Returns:
        A list of line numbers containing '---HUST_CHATBOT---' matching the condition.
    """

    line_numbers = []
    with open(file_path, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        for i in range(len(lines) - 1):
            # Regex to match the desired patterns
            if re.search(
                r"(^[1-9]\.$|(?:\b[IVX]{1,3}\.|10\.|[A-E]\.|\s[a-e]\.|\s[1-9]\.))$",  # Match conditions
                lines[i].rstrip()
            ) and lines[i + 1].strip() == '---HUST_CHATBOT---':
                line_numbers.append(i + 2)
    return line_numbers

def process_markdown_files(folder_path):
    """
    Processes all markdown files in the given folder to find matching lines.

    Args:
        folder_path: Path to the folder containing markdown files.

    Returns:
        A dictionary where each key is a filename and the value is a list of matching line numbers.
    """

    results = {}
    markdown_files = glob.glob(os.path.join(folder_path, '*.md'))

    for md_file in markdown_files:
        line_numbers = find_hust_chatbot_lines(md_file)
        if line_numbers:
            results[md_file] = line_numbers

    return results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python find_lines.py <my_folder>")
        sys.exit(1)

    folder_path = sys.argv[1]

    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        sys.exit(1)

    results = process_markdown_files(folder_path)

    if not results:
        print("No matches found.")
    else:
        for file, lines in results.items():
            print(f"{file}: {', '.join(map(str, lines))}")