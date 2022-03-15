from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

import openai 
import time

from credentials import openai_key
from os.path import exists
import pathlib
import pdfplumber
import numpy as np


from transformers import pipeline
summarizer = pipeline("summarization")

# to save
import pickle

if (exists("data.pickle")):
    file_to_read = open("data.pickle", "rb")
    prev_log = pickle.load(file_to_read)
else :
    prev_log = {}

#supress all warnings
# import warnings
# warnings.filterwarnings("ignore")

# initialising for selenium
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

# opening up whatsapp
driver.get("https://web.whatsapp.com/")
input("Press anything after QR scan")
time.sleep(1)

#initialising open ai
openai.api_key = openai_key["key"]
completion = openai.Completion()

# looking for group/contact
name = "Tanushree"

# this is where pdf will be stored
download_path = "C:\\Users\\aonno\\Downloads\\"

def showPaperSummary(pdfpath):
    tldr_tag = "\n tl;dr:"
    engine_list = openai.Engine.list() 

    paperFilePath = pdfpath
    paperContent = pdfplumber.open(paperFilePath).pages

    bot_response = []

    for i, page in enumerate(paperContent):    
        print(f"looking at page {i}.")
        text = page.extract_text() + tldr_tag
        
        print("text: ", text)

        summarized = summarizer(text, min_length=75, max_length=300)

        print( "summary: ", summarized[0]['summary_text'])

        bot_response.append(summarized[0]['summary_text'])
    return bot_response


def find_all_pdfs(name):

    save_file = open("savefile", "a", encoding="UTF-8")
    print("\nsearching for ", name)
    driver.find_element(By.XPATH, "(//div[@role='textbox'])[1]").send_keys(name)
    driver.find_element(By.XPATH, "(//div[@role='textbox'])[1]").send_keys(Keys.RETURN)
    time.sleep(2)

    # we need all documents
    print("\nLooking for pdfs\n")
    all_docs = driver.find_elements(By.XPATH, "(//div[@class='M_gdf'])")
    print(all_docs)
    bot_response = {}

    for i, t in enumerate(all_docs):
        pdfpath = download_path
        splitting = t.text.split("\n")
        who = splitting[0]
        when = splitting[-1]
        print(splitting)
        if (len(splitting) == 3):
            pdf_name = splitting[0]
        elif (len(splitting) == 5):
            pdf_name = splitting[2]
        else:
            pdf_name = splitting[1]

        print(i, " : ", pdf_name)
        print("by : ", who )
        
        if ".pdf" in pdf_name:
            print(pdf_name)
            pdfpath += pdf_name
            
            file_exists = exists(pdfpath)
            if (file_exists):
                print('file already downloaded.')
            else:
                driver.find_element(By.XPATH, f"(//span[@data-testid='audio-download'])[{i+1}]").click()
                # input('Getting the first download. input to continue')
            
            print(pdfpath)

            if when not in prev_log:
                print(f"procesing {when}")
                bot_response[when] = [showPaperSummary(pdfpath), who]
                prev_log[when] = bot_response[when] # for saving
            else :
                print(f"{when} already processed")
        
        else:
            print(f'no pdf here in {pdf_name}!')

       
    # now we generate the message 
    for k, v in bot_response.items():
        print(k, ":", v)
        useful_message = ".".join([x for x in v[0] if len(x)>0])
        MESSAGE = f"fanbot: pdf summary. Sent by: {v[1]}. Summary : {useful_message}."
        driver.find_element(By.XPATH("//div[@title='Type a message']")).send_keys(f"{MESSAGE}. time stamp: {str(time.time())}")
        driver.find_element(By.XPATH("//div[@title='Type a message']")).send_keys(Keys.RETURN)


find_all_pdfs("Study")

# saving all prev_log
file_to_read.close()

file_to_write = open("data.pickle", "wb")
pickle.dump(prev_log, file_to_write)
