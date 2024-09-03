import re
import sys
import os

def clean_html_from_markdown(html_string):
    """Cleans HTML tags from a Markdown string, handling various tags and lists."""

    # Remove specific tags while preserving content
    for tag in ['div', 'span', 'li', 'ul', 'ol', 'p', 'em','b', 'h1','i', 'figure', 'a', 'u', 'h4', 'h3', 'h2', 'h5', 'h6', 'hr']:
        html_string = re.sub(rf'<{tag}[^>]*>', '', html_string)
        html_string = re.sub(rf'</{tag}>', '', html_string)

    # Handle other tags
    html_string = re.sub(r'<\/?strong[^>]*>', '**', html_string)
    html_string = re.sub(r'<a.*?href="(.*?)".*?>(.*?)<\/a>', r'\2 (\1)', html_string)

    # Handle images 
    html_string = re.sub(r'<img.*?alt="(.*?)".*?>', r'\1', html_string)
#    html_string = re.sub(r'<img.*?>', '', html_string)  # Remove images without alt text

    # Handle unordered lists
    html_string = re.sub(r'\s*\n\s*- ', '\n- ', html_string)  

    # Handle ordered lists
    html_string = re.sub(r'\s*\n\s*1\. ', '\n1. ', html_string)

    # Handle HTML tables
    html_string = re.sub(r'<table.*?>.*?</table>',
                           lambda match: clean_html_table_from_markdown(match.group(0)),
                           html_string,
                           flags=re.DOTALL)

    return html_string.strip()

def clean_html_table_from_markdown(html_string):
    """Cleans HTML table code, extracts data, formats as Markdown table."""

    rows = re.findall(r'<tr>(.*?)</tr>', html_string, re.DOTALL)
    table_data = []
    for row in rows:
        cells = re.findall(r'<td.*?>(.*?)</td>', row, re.DOTALL)
        cleaned_cells = [re.sub(r'<.*?>', '', cell).strip() for cell in cells]
        table_data.append(cleaned_cells)

    markdown_table = ""
    if table_data: 
        markdown_table += "| " + " | ".join(table_data[0]) + " |\n" 
        markdown_table += "|---" * len(table_data[0]) + "|\n"
        for row in table_data[1:]:
            row_str = "| " + " | ".join(row) + " |\n" 
            markdown_table += row_str

    return markdown_table

def clean_markdown_file(file_path):
    """Cleans HTML, fixes spacing, and adds title in a Markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    cleaned_content = clean_html_from_markdown(markdown_content)
    cleaned_content = re.sub(r'\n\n\n+', '\n\n', cleaned_content)


    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)

    print(f"Cleaned HTML tags, fixed spacing, and added title in '{file_path}'")

def clean_markdown_folder(folder_path):
    """Cleans all .md files in a given folder."""
    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            file_path = os.path.join(folder_path, filename)
            clean_markdown_file(file_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python clean_markdown.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    clean_markdown_folder(folder_path)