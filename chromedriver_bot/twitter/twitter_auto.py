# PYTHON Example
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

import time 

#driver initialisation
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

#Change chrome driver path accordingly
chrome_driver = "chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

hashtag = "#AI"

driver.get('https://twitter.com/search?q =%23'+hashtag+'&src=typed_query&f=live')
 
time.sleep(3)
 
        # using set so that only unique links
        # are present and to avoid unnecessary repetition
links = set()
 
        # obtaining the links of the tweets
for _ in range(2):
            # executing javascript code
            # to scroll the webpage
    driver.execute_script(
                'window.scrollTo(0, document.body.scrollHeight)'
            )
 
    time.sleep(4)
 
            # using list comprehension
            # for adding all the tweets link to the set
            # this particular piece of code might
            # look very complicated but the only reason
            # I opted for list comprehension because is
            # lot faster than traditional loops
    [ links.add(elem.get_attribute('href')) for elem in driver.find_elements_by_xpath("//a[@dir ='auto']") ]

print(">>>>>>>>>>>>>>>>>>>>\n",links)


# traversing through the generated links
for link in links:
            # opens individual links
    driver.get(link)
    time.sleep(4)
 
    try:
                # retweet button selector
        elem = driver.find_element_by_css_selector('.css-18t94o4[data-testid ="retweet"]')
        print(elem)
                # initializes action chain
        #actions = ActionChains(driver)
                # sends RETURN key to retweet without comment
        #actions.send_keys(Keys.RETURN).perform()
 
                # like button selector
        elem = driver.find_element_by_css_selector('.css-18t94o4[data-testid ="like"]')
        print(elem)
                # adding higher sleep time to avoid
                # getting detected as bot by twitter
        time.sleep(10)
    except Exception as e:
        print(e, "sleep for 2 secs.")
        time.sleep(2)

# driver.get("https://twitter.com/SolanaCookbook")

# driver.find_element_by_css_selector('')
