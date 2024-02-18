import os
import PyPDF2
import re
import json
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def combine_pdf_text(folder_path):
    combined_results = []

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
                    combined_results.append({
                        "file": filename,
                        "page_number": page_num + 1,
                        "text": text
                    })

    # Write the combined results to a JSON file
    combined_file_path = os.path.join(folder_path, "combined_results.json")
    with open(combined_file_path, 'w') as combined_file:
        json.dump(combined_results, combined_file)

    return combined_file_path

def find_text_in_combined_text(combined_file_path, search_text):
    found_results = []

    # Read the combined results from the JSON file
    with open(combined_file_path, 'r') as combined_file:
        combined_results = json.load(combined_file)

    # Search for the text and get page number
    for result in combined_results:
        if re.search(r"\b" + re.escape(search_text) + r"\b", result['text'], re.IGNORECASE):
            found_results.append(result)

    return found_results

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path_entry.delete(0, tk.END)
        folder_path_entry.insert(0, folder_selected)

def search_text():
    folder_path = folder_path_entry.get()
    search_text = search_text_entry.get()

    if not folder_path or not search_text:
        messagebox.showwarning("Warning", "Please provide folder path and search text.")
        return

   
    results = find_text_in_combined_text(combined_file_path, search_text)

    if results:
        result_text.delete('1.0', tk.END)
        for i, result in enumerate(results, start=1):
            result_text.insert(tk.END, f"Result {i}:\n")
            result_text.insert(tk.END, f"File: {result['file']}, Page: {result['page_number']}\n")
            result_text.insert(tk.END, f"Text: {result['text']}\n\n")
    else:
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, "No results found.")

# Create the main window
root = tk.Tk()
root.title("PDF Text Search")

# Folder Path
folder_label = tk.Label(root, text="Folder Path:")
folder_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

folder_path_entry = tk.Entry(root, width=50)
folder_path_entry.grid(row=0, column=1, padx=5, pady=5)

folder_path = 'pdf_repo'
combined_file_path = combine_pdf_text(folder_path)
   

browse_button = tk.Button(root, text="Browse", command=browse_folder)
browse_button.grid(row=0, column=2, padx=5, pady=5)

# Search Text
search_label = tk.Label(root, text="Search Text:")
search_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

search_text_entry = tk.Entry(root, width=50)
search_text_entry.grid(row=1, column=1, padx=5, pady=5)

search_button = tk.Button(root, text="Search", command=search_text)
search_button.grid(row=1, column=2, padx=5, pady=5)

# Results
result_label = tk.Label(root, text="Search Results:")
result_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

result_text = scrolledtext.ScrolledText(root, width=80, height=20)
result_text.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
