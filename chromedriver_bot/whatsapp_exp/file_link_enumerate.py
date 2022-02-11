import bs4 as bs
import urllib.request
import re
scraped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/Reinforcement_learning')
article = scraped_data.read()
parsed_article = bs.BeautifulSoup(article,'lxml')
paragraphs = parsed_article.find_all('p')
article_text = ""
for p in paragraphs:
    article_text += p.text