import os
import re
import sys

def remove_tones(text):
  """Removes Vietnamese tone marks from a string."""
  text = text.replace('á', 'a').replace('à', 'a').replace('ả', 'a').replace('ã', 'a').replace('ạ', 'a')
  text = text.replace('ă', 'a').replace('ắ', 'a').replace('ằ', 'a').replace('ẳ', 'a').replace('ẵ', 'a').replace('ặ', 'a')
  text = text.replace('â', 'a').replace('ấ', 'a').replace('ầ', 'a').replace('ẩ', 'a').replace('ẫ', 'a').replace('ậ', 'a')
  text = text.replace('é', 'e').replace('è', 'e').replace('ẻ', 'e').replace('ẽ', 'e').replace('ẹ', 'e')
  text = text.replace('ê', 'e').replace('ế', 'e').replace('ề', 'e').replace('ể', 'e').replace('ễ', 'e').replace('ệ', 'e')
  text = text.replace('í', 'i').replace('ì', 'i').replace('ỉ', 'i').replace('ĩ', 'i').replace('ị', 'i')
  text = text.replace('ó', 'o').replace('ò', 'o').replace('ỏ', 'o').replace('õ', 'o').replace('ọ', 'o')
  text = text.replace('ô', 'o').replace('ố', 'o').replace('ồ', 'o').replace('ổ', 'o').replace('ỗ', 'o').replace('ộ', 'o')
  text = text.replace('ơ', 'o').replace('ớ', 'o').replace('ờ', 'o').replace('ở', 'o').replace('ỡ', 'o').replace('ợ', 'o')
  text = text.replace('ú', 'u').replace('ù', 'u').replace('ủ', 'u').replace('ũ', 'u').replace('ụ', 'u')
  text = text.replace('ư', 'u').replace('ứ', 'u').replace('ừ', 'u').replace('ử', 'u').replace('ữ', 'u').replace('ự', 'u')
  text = text.replace('ý', 'y').replace('ỳ', 'y').replace('ỷ', 'y').replace('ỹ', 'y').replace('ỵ', 'y')
  text = text.replace('đ', 'd')
  # Uppercase
  text = text.replace('Á', 'a').replace('À', 'a').replace('Ả', 'a').replace('Ã', 'a').replace('Ạ', 'a')
  text = text.replace('Ă', 'a').replace('Ắ', 'a').replace('Ằ', 'a').replace('Ẳ', 'a').replace('Ẵ', 'a').replace('Ặ', 'a')
  text = text.replace('Â', 'a').replace('Ấ', 'a').replace('Ầ', 'a').replace('Ẩ', 'a').replace('Ẫ', 'a').replace('Ậ', 'a') 
  text = text.replace('É', 'e').replace('È', 'e').replace('Ẻ', 'e').replace('Ẽ', 'e').replace('Ẹ', 'e')
  text = text.replace('Ê', 'e').replace('Ế', 'e').replace('Ề', 'e').replace('Ể', 'e').replace('Ễ', 'e').replace('Ệ', 'e')
  text = text.replace('Í', 'i').replace('Ì', 'i').replace('Ỉ', 'i').replace('Ĩ', 'i').replace('Ị', 'i')
  text = text.replace('Ó', 'o').replace('Ò', 'o').replace('Ỏ', 'o').replace('Õ', 'o').replace('Ọ', 'o')
  text = text.replace('Ô', 'o').replace('Ố', 'o').replace('Ồ', 'o').replace('Ổ', 'o').replace('Ỗ', 'o').replace('Ộ', 'o')
  text = text.replace('Ơ', 'o').replace('Ớ', 'o').replace('Ờ', 'o').replace('Ở', 'o').replace('Ỡ', 'o').replace('Ợ', 'o')
  text = text.replace('Ú', 'u').replace('Ù', 'u').replace('Ủ', 'u').replace('Ũ', 'u').replace('Ụ', 'u')
  text = text.replace('Ư', 'u').replace('Ứ', 'u').replace('Ừ', 'u').replace('Ử', 'u').replace('Ữ', 'u').replace('Ự', 'u')
  text = text.replace('Ý', 'y').replace('Ỳ', 'y').replace('Ỷ', 'y').replace('Ỹ', 'y').replace('Ỵ', 'y')
  text = text.replace('Đ', 'd')   
  return text


def clean_title(title):
  """Cleans the title by removing tones, punctuation, and extra spaces."""
  title = re.sub(r'[\[\]\,!?:/()"]', '', title)  # Remove brackets and punctuation
  title = remove_tones(title)
  title = ''.join(word.capitalize() for word in title.split())
  return title

def rename_markdown_files(directory):
  """Renames Markdown files based on their processed H1 titles."""
  markdown_files = [f for f in os.listdir(directory) if f.endswith('.md')]
  for count, filename in enumerate(markdown_files):
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'^# (.*)', content, re.MULTILINE)
    if match:
      raw_title = match.group(1).strip()
      new_title = clean_title(raw_title)
    else:
      print(f"Warning: No H1 heading found in '{filename}'. Skipping.")
      continue

    new_filename = f"hust_{count+1}_{new_title}.md"

    old_path = os.path.join(directory, filename)
    new_path = os.path.join(directory, new_filename)
    os.rename(old_path, new_path)

    print(f"Renamed '{filename}' to '{new_filename}'")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rename_markdown.py <target_folder>")
        sys.exit(1)

    target_directory = sys.argv[1]
    rename_markdown_files(target_directory)