# PYTHON Example
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

import time 
from open_ai_bot_experiment import *


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

# OpenAI initialisation.

openai.api_key = openai_key["key"]
completion = openai.Completion()

start_sequence = '\nfanbot:'
restart_sequence = '\n\nyou:'

f1 = open('extracted_tanu_whatsapp.txt', 'r+', encoding='UTF-8')
session_prompt = f1.readlines()

session_prompt = session_prompt[0:2100]
#print(session_prompt)
print("length of session prompt: ", len(session_prompt), '. Open ai bot initialised.')


def send_messages(names):
    for name in names:
        print("sending for ", name)
        driver.find_element_by_xpath(f"//span[@title='{name}']").click() 

        time.sleep(2)

        driver.find_element_by_xpath("//div[@title='Type a message']").send_keys(f"This is bot generated message. Sorry for the trouble. Message at {str(time.time())}")
        driver.find_element_by_xpath("//div[@title='Type a message']").send_keys(Keys.RETURN)

def search_and_send_messages(names):
    for name in names:
        print("searching for ", name)
        driver.find_element_by_xpath("(//div[@role='textbox'])[1]").send_keys(name)
        driver.find_element_by_xpath("(//div[@role='textbox'])[1]").send_keys(Keys.RETURN)
        time.sleep(2)

        driver.find_element_by_xpath("//div[@title='Type a message']").send_keys(f"This is bot generated message. Sorry for the trouble. Message at {str(time.time())}")
        driver.find_element_by_xpath("//div[@title='Type a message']").send_keys(Keys.RETURN)

def search_and_send_custom_messages(names):
    #previous chat wouldbe considered
    for name in names:
        print("\nsearching for ", name, "\n")
        driver.find_element_by_xpath("(//div[@role='textbox'])[1]").send_keys(name)
        driver.find_element_by_xpath("(//div[@role='textbox'])[1]").send_keys(Keys.RETURN)
        time.sleep(2)

        print("\nlooking for last message\n")
        last_text = driver.find_element_by_xpath("(//div[@class='_22Msk'])[last()]").text # not working
        print(f"found: {last_text}")
        output_text = chatter_bot_interaction(last_text)
        print('you:', output_text)
        driver.find_element_by_xpath("//div[@title='Type a message']").send_keys(output_text+ "\n" + last_text)
        driver.find_element_by_xpath("//div[@title='Type a message']").send_keys(Keys.RETURN)


def chatter_bot_interaction(input_text):
    print("input : ", input_text)
    
    response = "Hi! its your friendly neighborhood fanbot. I am trying to extract your last communication to me. I guess it is: "
    print("Bot Response:", response)
    response = f":: msg at {str(time.perf_counter())} :: {response}"
    if(response):
        return response
    else :
        return f"fan bot is offline right now."



def chat_with_a_person(name, session_prompt):
    continue_chat = True
    prev_timestamp = 0

    # get to dms
    print("\nsearching for ", name, "\n")
    driver.find_element_by_xpath("(//div[@role='textbox'])[1]").send_keys(name)
    driver.find_element_by_xpath("(//div[@role='textbox'])[1]").send_keys(Keys.RETURN)
    time.sleep(2)

    while(1):
        print(f"\nlooking for last message, continue_chat: {continue_chat}\n")
        last_text = driver.find_element_by_xpath("(//div[@class='_22Msk'])[last()]").text.split('\n')
        print(last_text)
        if(len(last_text)<2):
            last_timestamp = last_text[0]
            last_text = ""
        else :
            last_timestamp = last_text[1]
            if('fanbot :' in last_text[0]):
                last_text = last_text[0].split('fanbot :')[1].strip()
            else:
                last_text = last_text[0].strip()

        print("\n",last_timestamp, last_text, "\n")
        # output_text = chatter_bot_interaction(last_text)
        # print('you:', output_text)
        
        if (last_text == "fanbot stop"):
            continue_chat = True
        elif (last_text == "fanbot start"):
            continue_chat = False
        elif(last_text == "fanbot help"):
            driver.find_element_by_xpath("//div[@title='Type a message']").send_keys("ask ashwin.")
            driver.find_element_by_xpath("//div[@title='Type a message']").send_keys(Keys.RETURN)
    
        if (continue_chat):
            incoming_msg = last_text
            #print(incoming_msg)

            # to check whether I am replying to myself
            if(prev_timestamp != last_timestamp):
                print(f"you: {incoming_msg}")
                time.sleep(2)
                answer = ask(incoming_msg, session_prompt)
                print(f"fanbot: {answer}")
                a = input('press a to continue and send.')
                if(a.lower() =='a'):
                    session_prompt = append_interaction_to_chat_log(incoming_msg, answer, session_prompt)
                    # driver.find_element_by_xpath("//div[@title='Type a message']").send_keys('fanbot: '+answer)
                    # driver.find_element_by_xpath("//div[@title='Type a message']").send_keys(Keys.RETURN)
                else:
                    continue
            else: 
                answer = f"No response from the other side. bye." 
                print(answer)
                # driver.find_element_by_xpath("//div[@title='Type a message']").send_keys('fanbot: '+answer)
                # driver.find_element_by_xpath("//div[@title='Type a message']").send_keys(Keys.RETURN)
                break
        
        prev_timestamp = last_timestamp


print("Calling chat_with_a_person().")
# search_and_send_custom_messages(names)
#chat_with_a_person("Tanushree", session_prompt)
call_bot(session_prompt)


