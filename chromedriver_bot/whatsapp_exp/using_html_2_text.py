import html2text
from urllib.request import urlopen

h = html2text.HTML2Text()

h.ignore_links = True


url = "https://en.wikipedia.org/wiki/Aaron_Swartz"
html = urlopen(url).read()

html = str(html)
print(h.handle(html))

