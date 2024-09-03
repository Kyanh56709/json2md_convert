import re
import sys

def clean_html_table_from_markdown(html_string):
    """Cleans HTML table code, extracts data, formats as Markdown table."""

    rows = re.findall(r'<tr>(.*?)</tr>', html_string, re.DOTALL)
    table_data = []
    for row in rows:
        cells = re.findall(r'<td.*?>(.*?)</td>', row, re.DOTALL)
        cleaned_cells = [re.sub(r'<.*?>', '', cell).strip() for cell in cells]
        table_data.append(cleaned_cells)

    markdown_table = ""
    for row in table_data:
        row_str = "| " + " | ".join(row) + " |\n" 
        markdown_table += row_str

    return markdown_table

def clean_markdown_file(file_path):
    """Cleans HTML and fixes spacing in a Markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    # 1. Clean general HTML tags
    cleaned_content = re.sub(r'<.*?>', '', markdown_content)

    # 2. Clean HTML tables 
    cleaned_content = re.sub(r'<table.*?>.*?</table>', 
                           lambda match: clean_html_table_from_markdown(match.group(0)), 
                           cleaned_content, 
                           flags=re.DOTALL)

    # 3. Fix spacing around table rows
    cleaned_content = re.sub(r'\n\n\n+', '\n\n', cleaned_content)  # Remove excessive newlines

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)

    print(f"Cleaned HTML tags and fixed spacing in '{file_path}'")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python clean_markdown.py <markdown_file.md>")
        sys.exit(1)

    markdown_file = sys.argv[1]
    clean_markdown_file(markdown_file)