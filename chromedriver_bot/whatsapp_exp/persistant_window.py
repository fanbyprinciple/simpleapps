# PYTHON Example
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#Change chrome driver path accordingly
chrome_driver = "chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

driver.get("https://selenium-python.readthedocs.io/locating-elements.html")

elem = driver.find_element(By.XPATH, '//*[@id="searchbox"]/div/form/input[1]')
elem.click()
elem.send_keys("HOw you doing")


# # all_elements = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/section/div/div/div[2]/div/div/div')
# all_conversation_elements = driver.find_elements_by_xpath('//span[contains(text(), "T")]')
# print( all_conversation_elements)

# for i in all_conversation_elements:
#     i.click()

# # its working but not able to locate elements
