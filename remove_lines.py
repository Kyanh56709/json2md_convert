import os
import sys

def remove_lines_from_md(folder_path):
  """
  Removes lines 2-18 from all Markdown (.md) files in a specified folder.

  Args:
    folder_path: The path to the folder containing the .md files.
  """
  for filename in os.listdir(folder_path):
    if filename.endswith(".md"):
      file_path = os.path.join(folder_path, filename)
      with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

      modified_lines = lines[:1] + lines[20:] 

      with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(modified_lines)

  print(f"Lines 2-18 removed from all .md files in {folder_path}") 

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python remove_lines.py <target_folder>")
    sys.exit(1) 

  target_folder = sys.argv[1]
  remove_lines_from_md(target_folder)