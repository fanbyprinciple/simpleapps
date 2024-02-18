import os
import PyPDF2
import re

def find_text_in_pdfs(folder_path, search_text):
    found_results = []

    # Iterate through each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                num_pages = len(pdf_reader.pages)

                # Iterate through each page in the PDF
                for page_num in range(num_pages):
                    page = pdf_reader.pages[page_num]
                    text = page.extract_text()

                    # Search for the text and get page number
                    match = re.search(r"\b" + re.escape(search_text) + r"\b", text, re.IGNORECASE)
                    if match:
                        start_index = max(0, match.start() - 200)
                        end_index = min(len(text), match.end() + 200)
                        context = text[start_index:end_index]

                        # Append the result
                        found_results.append({
                            "file": filename,
                            "page_number": page_num + 1,
                            "context": context
                        })

    return found_results

# Example usage
folder_path = 'pdf_repo'
search_text = 'Nessler Cylinder'
results = find_text_in_pdfs(folder_path, search_text)

if results:
    print("Search results:")
    for result in results:
        print("\n")
        print(f"File: {result['file']}, Page: {result['page_number']}")
        print("Context:")
        print(result['context'])
        print()
else:
    print("No results found.")