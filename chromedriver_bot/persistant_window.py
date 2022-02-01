# PYTHON Example
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#Change chrome driver path accordingly
chrome_driver = "chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

driver.get("https://www.twitter.com/messages")

# all_elements = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/section/div/div/div[2]/div/div/div')
all_conversation_elements = driver.find_elements_by_xpath('//span[contains(text(), "T")]')
print( all_conversation_elements)

for i in all_conversation_elements:
    i.click()

# its working but not able to locate elements
