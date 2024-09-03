import os
import glob
import sys

def remove_asterisks_from_file(file_path):
    """Removes all asterisks (*) from a file.

    Args:
        file_path (str): The path to the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        content = content.replace('*', '')

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Removed asterisks from: {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def remove_asterisks_from_folder(folder_path):
    """Removes all asterisks (*) from all .md files in a folder.

    Args:
        folder_path (str): The path to the folder.
    """
    for filename in glob.glob(os.path.join(folder_path, '*.md')):
        remove_asterisks_from_file(filename)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python remove_asterisks.py <my_folder>")
        sys.exit(1)

    folder_path = sys.argv[1]

    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        sys.exit(1)

    remove_asterisks_from_folder(folder_path)