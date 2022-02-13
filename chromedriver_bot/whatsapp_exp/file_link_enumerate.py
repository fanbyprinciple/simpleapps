from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.youtube.com/watch?v=hcMzwMrr1tE"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

#print(text)


split_array = text.split('\n')
final = ""
for t in split_array:
    if len(t.split(' '))>4:
        final += "\n"+ t
 
f = open('file_output', 'w+', encoding='UTF-8')

f.write(final)

# codefor text summarisation
# import openai 
# from credentials import openai_key

# openai.api_key = openai_key["key"]
# completion = openai.Completion()

# response = openai.Completion.create(engine="davinci",prompt=final,temperature=0.3,
#             max_tokens=140,
#             top_p=1,
#             frequency_penalty=0,
#             presence_penalty=0,
#             stop=["\n"]
#         )

# print(response)
