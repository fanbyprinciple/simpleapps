import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure you've downloaded the stopwords dataset from NLTK
nltk.download('stopwords')  # Uncomment this line if you haven't downloaded stopwords yet
nltk.download('punkt')  # For tokenization

# Define the path to your Excel file
file_path = '.\pdf_repo\Animalstudy_12Feb2024.xlsx'  # Update this to your actual file path

# Load the Excel file into a pandas DataFrame
df = pd.read_excel(file_path)

# Assuming the article titles are in a column named 'Article Title'
column_name = 'Article Title'  # Update this if your column name is different

common_stopwords = []
common = open('./common.txt', 'r').readlines()

print(common)

for i in common:
    common_stopwords.append(i.strip())

# Load stopwords from NLTK
stop_words = set(common_stopwords)

print(stop_words)

# Function to extract keywords from a title using NLTK for tokenization and stopwords removal
def extract_keywords(title): 
    words = word_tokenize(title.lower())  # Tokenize and convert to lowercase
    words = [word for word in words if len(word) > 3]
    keywords = [word for word in words if word not in stop_words and word.isalpha()]
    return keywords

# Initialize an empty dictionary to store the serial number and keywords
keywords_dict = {}

# Iterate through the DataFrame, extracting keywords for each title
for index, row in df.iterrows():
    title = row[column_name]
    keywords = extract_keywords(title)
    keywords_dict[index + 1] = keywords  # Assuming serial number starts at 1 and matches the row index + 1

# Print the resulting dictionary
# Define the path to your output text file
output_file_path = 'keywords_output.txt'  # Update this with your desired output file path

# Write the resulting dictionary to a text file
with open(output_file_path, 'w') as f:
    for key, value in keywords_dict.items():
        try:
            f.write(f"{key}: {value}\n")
        except:
            continue
    