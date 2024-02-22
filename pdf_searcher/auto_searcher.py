import fitz  # PyMuPDF
import os
import re

# Function to read keywords and their serial numbers from the file
def read_keywords(file_path):
    keywords_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(': ')
            serial_number = parts[0]
            keywords = eval(parts[1])  # Convert string list representation to actual list
            keywords_dict[serial_number] = keywords
    return keywords_dict

# Function to search PDFs for keywords and keep association with serial numbers
def search_pdfs(keywords_dict, pdf_repo, output_file_path):
    results_dict = {serial: [] for serial in keywords_dict}

    for filename in os.listdir(pdf_repo):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_repo, filename)
            doc = fitz.open(pdf_path)

            for page in doc:
                text = page.get_text("text")

                # Ensure text is treated as UTF-8
                text = text.encode('utf-8', errors='ignore').decode('utf-8', errors='ignore')

                with open('all_text', 'a', encoding='utf-8') as text1:  # Specify encoding here
                    try:
                        text1.write(text.lower())
                    except Exception as e:
                        print(f'<Enc error: {str(e)}>')

                words = text.split()

                for serial_number, keywords in keywords_dict.items():
                    for keyword in keywords:
                        keyword_regex = re.compile(r'\b' + re.escape(keyword.lower()) + r'\b')
                        if keyword_regex.search(text.lower()):

                            start_indices = [i for i, word in enumerate(words) if keyword.lower() in word.lower()]
                            for start in start_indices:
                                start_idx = max(start - 50, 0)
                                end_idx = min(start + 50, len(words))
                                excerpt = ' '.join(words[start_idx:end_idx])
                                entry = f"{keyword}> {filename} - Page {page.number + 1}: {excerpt}\n"
                                results_dict[serial_number].append(entry)

    with open(output_file_path, 'w', encoding='utf-8') as f:  # Ensure UTF-8 encoding
        for serial in sorted(results_dict, key=lambda x: int(x)):
            for result in results_dict[serial]:
                try:
                    f.write(f"Serial {serial}, {result}")
                except UnicodeEncodeError as e:
                    f.write(f'<enc_err: {str(e)}>\n')


# File paths
keywords_file = './keywords_output.txt'  # Update this path
pdf_repo = './pdf_repo'  # Update this path to your PDF directory
output_file_path = 'search_results_with_serial.txt'  # Update this path if needed

# Read keywords and their serial numbers
keywords_dict = read_keywords(keywords_file)

# keywords_dict = {1 : ['catappa']}
# Perform the search
search_pdfs(keywords_dict, pdf_repo, output_file_path)