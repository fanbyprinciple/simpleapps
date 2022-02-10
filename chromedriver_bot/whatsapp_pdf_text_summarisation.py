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
import wget
import pathlib
import pdfplumber
import numpy as np

#supress all warnings
# import warnings
# warnings.filterwarnings("ignore")

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

#Change chrome driver path accordingly
chrome_driver = "chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

# whatsapp specific code
driver.get("https://web.whatsapp.com/")

input("Press anything after QR scan")
time.sleep(1)


openai.api_key = openai_key["key"]
completion = openai.Completion()

name = "Tanushree"
download_path = "C:\\Users\\aonno\\Downloads\\"

def showPaperSummary(pdfpath):
    tldr_tag = "\n tl;dr:"
    engine_list = openai.Engine.list() 

    paperFilePath = pdfpath
    paperContent = pdfplumber.open(paperFilePath).pages

    for page in paperContent:    
        text = page.extract_text() + tldr_tag
        response = openai.Completion.create(engine="davinci",prompt=text,temperature=0.3,
            max_tokens=140,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n"]
        )
        print(response["choices"][0]["text"])


def find_all_pdfs(name):
    print("searching for ", name)
    driver.find_element(By.XPATH, "(//div[@role='textbox'])[1]").send_keys(name)
    driver.find_element(By.XPATH, "(//div[@role='textbox'])[1]").send_keys(Keys.RETURN)
    time.sleep(2)

    # print("\nlooking for message\n")
    # all_text = driver.find_elements(By.XPATH, "(//div[@class='_22Msk'])")

    # we need all documents
    print("\nLooking for pdfs\n")
    all_docs = driver.find_elements(By.XPATH, "(//div[@class='M_gdf'])")
    print(all_docs)
    for i, t in enumerate(all_docs):
        pdfpath = download_path
        splitting = t.text.split("\n")
        print(splitting)
        if (len(splitting) == 3):
            pdf_name = splitting[0]
        elif (len(splitting) == 5):
            pdf_name = splitting[2]
        else:
            pdf_name = splitting[1]

        print(i, " : ", pdf_name)
        
        
        if ".pdf" in pdf_name:
            print(pdf_name)
            pdfpath += pdf_name
            

            file_exists = exists(pdfpath)
            if (file_exists):
                print('file already downloaded.')
            else:
                driver.find_element(By.XPATH, f"(//span[@data-testid='audio-download'])[{i+1}]").click()
                input('Getting the first download. input to continue')
        else:
            print(f'no pdf here in {pdf_name}!')

       
        print(pdfpath)

        showPaperSummary(pdfpath)

    #driver.find_element(By.XPATH("//div[@title='Type a message']")).send_keys(f"This is bot generated message. Sorry for the trouble. Message at {str(time.time())}")
    #driver.find_element(By.XPATH("//div[@title='Type a message']")).send_keys(Keys.RETURN)


find_all_pdfs("Study")