import os
import glob
import sys

def count_characters_in_file(file_path):
    """Counts the total number of characters in a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        int: The total number of characters in the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            return len(content)
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return 0

def count_characters_in_folder(folder_path):
    """Counts the total number of characters in all .md files in a folder.

    Args:
        folder_path (str): The path to the folder.

    Returns:
        int: The total character count across all .md files.
    """
    total_characters = 0
    for filename in glob.glob(os.path.join(folder_path, '*.md')):
        total_characters += count_characters_in_file(filename)
    return total_characters

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_characters.py <my_folder>")
        sys.exit(1)

    folder_path = sys.argv[1]

    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        sys.exit(1)

    total_count = count_characters_in_folder(folder_path)
    print(f"Total characters in all .md files: {total_count}")