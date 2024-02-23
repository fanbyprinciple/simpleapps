import fitz  # PyMuPDF
import os

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
    results = []

    for filename in os.listdir(pdf_repo):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_repo, filename)
            doc = fitz.open(pdf_path)

            for page in doc:
                text = page.get_text("text")
                words = text.split()

                for serial_number, keywords in keywords_dict.items():
                    for keyword in keywords:
                        if keyword in text:
                            start_indices = [i for i, word in enumerate(words) if keyword in word]
                            for start in start_indices:
                                start_idx = max(start - 50, 0)
                                end_idx = min(start + 50, len(words))
                                excerpt = ' '.join(words[start_idx:end_idx])
                                results.append(f"Serial {serial_number},{keyword}> {filename} - Page {page.number + 1}: {excerpt}\n")

    with open(output_file_path, 'w') as f:
        for result in results:
            try:
                f.write(result)
            except:
                f.write('<enc_err>')

    print(f"Search completed. Results written to {output_file_path}")

# File paths
keywords_file = './keywords_output.txt'  # Update this path
pdf_repo = './pdf_repo'  # Update this path to your PDF directory
output_file_path = 'search_results_with_serial.txt'  # Update this path if needed

# Read keywords and their serial numbers
keywords_dict = read_keywords(keywords_file)

print(keywords_dict)
# Perform the search
search_pdfs(keywords_dict, pdf_repo, output_file_path)