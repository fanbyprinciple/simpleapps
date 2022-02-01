from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from chatterbot import ChatBot
import time
from selenium.webdriver.chrome.options import Options
import pickle
import os

chrome_options = Options()
# chrome_options.add_argument("user-data-dir=selenium") 
# driver = webdriver.Chrome(chrome_options=chrome_options)

driver = webdriver.Chrome()

if os.path.exists("cookies.pkl"):
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

driver.get("https://www.google.com")

driver.find_element_by_xpath("//input").click()
driver.find_element_by_xpath("//input").send_keys("Carmen Sandiego")
driver.find_element_by_xpath("//input").send_keys(u'\ue007')

pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

# 8082
# 173.212.200.69:8082