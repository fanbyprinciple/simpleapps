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

def find_html_in_text(name):
    print("\nsearching for ", name, "\n")
    driver.find_element_by_xpath("(//div[@role='textbox'])[1]").send_keys(name)
    driver.find_element_by_xpath("(//div[@role='textbox'])[1]").send_keys(Keys.RETURN)
    time.sleep(2)

    print("going to top\n")

    days_back = 4
    for i in range(days_back):
        element = driver.find_element_by_xpath("(//div[@class='cvjcv EtBAv'])[2]")
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
    # print(all_texts)
    for t in all_texts:
        a = t.text.split("\n")

        for b in a:
            if "https" in b:
                # print(b+ "\n")
                only_link = "https" + b.split('https')[1].split(' ')[0]
                all_links.append(only_link)

    all_links = list(set(all_links))
    print(all_links)
    string_text = '\n'.join(all_links)

    driver.find_element_by_xpath("//div[@title='Type a message']").send_keys(f"Hello! These are all the links exchanged in last {days_back} days.\n {string_text}")
    driver.find_element_by_xpath("//div[@title='Type a message']").send_keys(Keys.RETURN)

print("Calling chat_with_a_person().")

#find_html_in_text("achu")
find_html_in_text("tanushree")


