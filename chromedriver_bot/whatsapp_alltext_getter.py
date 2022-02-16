# PYTHON Example
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

import time 

#supress all warnings
import warnings
warnings.filterwarnings("ignore")

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

#Change chrome driver path accordingly
chrome_driver = "chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

# whatsapp specific code
driver.get("https://web.whatsapp.com/")

input("Press anything after QR scan")
time.sleep(5)

#names = ["Achu Jio", "Tanushree", "Pallavi"]
#message = "Android auto messaging bot here, " +  name + "!"

#names = ["Tanushree"]
from transformers import pipeline

from urllib.request import urlopen
from bs4 import BeautifulSoup

def enumerate_link(urlink):    
    url = urlink
    try:
        html = urlopen(url).read()
        soup = BeautifulSoup(html, features="html.parser")

        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()    # rip it out

        text = ""

        for para in soup.find_all("p"):
            text += para.get_text()

        # get text
        text = soup.get_text()

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

    except Exception as e:
        
        text = "Unable to open link.\n"
    #print(text)

    split_array = text.split('\n')
    final = ""
    for t in split_array:
        if len(t.split(' '))>6:
            final += "\n"+ t
    
    f = open('file_output', 'w+', encoding='UTF-8')

    f.write(final)

def find_html_in_text(name):
    print("\nsearching for ", name, "\n")
    driver.find_element_by_xpath("(//div[@role='textbox'])[1]").send_keys(name)
    driver.find_element_by_xpath("(//div[@role='textbox'])[1]").send_keys(Keys.RETURN)
    time.sleep(2)

    print("going to top\n")

    days_back = 10
    for i in range(days_back):
        #element = driver.find_element_by_xpath("(//div[@class='cvjcv EtBAv'])[2]")
        element = driver.find_element_by_xpath("(//div[@class='_1Gy50'])[1]")
        print(element.text)

        coordinates = element.location_once_scrolled_into_view
        driver.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))
        time.sleep(1)
        # actions = ActionChains(driver)
        # actions.move_to_element(element).perform()

    print("\nlooking for all messages\n")
    all_texts = driver.find_elements(By.XPATH,"(//div[@class='_22Msk'])")

    # getting https

    all_links = []

    link_elements = []

    # print(all_texts)
    for t in all_texts:
        a = t.text.split("\n")
        
        for b in a:
            if "https" in b:
                # print(b+ "\n")
                only_link = "https" + b.split('https')[1].split(' ')[0]

                all_links.append(only_link)
                link_elements.append(t)

    all_links = list(set(all_links))
    print(all_links)

    result_list = []

    if(len(all_links) > 0):

        # driver.find_element_by_xpath("//div[@title='Type a message']").send_keys(f"Fanbot: Hello here we are summarising links from last few days.")
        # driver.find_element_by_xpath("//div[@title='Type a message']").send_keys(Keys.RETURN)

        for i, link in enumerate(all_links):
            enumerate_link(link)

            f = open('file_output', "r", encoding='utf-8')
            to_tokenize = str(f.read())

            if len(to_tokenize) > 1024:
                to_tokenize = to_tokenize[:1024]

            summarizer = pipeline("summarization")
            summarized = summarizer(to_tokenize, min_length=20, max_length=1024)

            result  = summarized[0]['summary_text']

            result_list.append(f"{i+1}. {all_links[i]} : {result}")
            
            # making a reply
            # elem = link_elements[i]
            # a = ActionChains(driver)
            # #m= driver.find_element_by_link_text("Enabled")
            # a.move_to_element(elem).perform()
            # down_arrow = driver.find_element(By.XPATH, "(//span[@data-testid='down-context'])[1]")
            # down_arrow.click()
            # #@(//div[@class='_1Gy50'])[1]

            # reply_button = driver.find_element(By.XPATH, "(//div[@aria-label='Reply'])[last()]")
            # reply_button.click()
        driver.find_element_by_xpath("//div[@title='Type a message']").send_keys("Fanbot: here is a short summary of links exchanged in past few days.")
        driver.find_element_by_xpath("//div[@title='Type a message']").send_keys(Keys.RETURN)
        driver.find_element_by_xpath("//div[@title='Type a message']").send_keys("\n".join(result_list))
        driver.find_element_by_xpath("//div[@title='Type a message']").send_keys(Keys.RETURN)
    else : 
        result = f"There were no links in last few messages."
        driver.find_element_by_xpath("//div[@title='Type a message']").send_keys(result)
        driver.find_element_by_xpath("//div[@title='Type a message']").send_keys(Keys.RETURN)

print("Calling chat_with_a_person().")

#find_html_in_text("achu")
find_html_in_text("tanushree")
