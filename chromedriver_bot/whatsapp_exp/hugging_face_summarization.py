# https://www.machinecurve.com/index.php/2020/12/21/easy-text-summarization-with-huggingface-transformers-and-machine-learning/

from transformers import pipeline

f = open('file_output', "r", encoding='utf-8')
to_tokenize = f.read()

summarizer = pipeline("summarization")
summarized = summarizer(to_tokenize, min_length=75, max_length=300)

print(summarized[0]['summary_text'])

