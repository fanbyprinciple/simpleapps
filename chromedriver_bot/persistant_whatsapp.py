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

from chatterbot import ChatBot
#bot = ChatBot('fan')

bot = ChatBot(
    'fan',  
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'],
)

#import ListTrainer
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

# trainer.train([
# 'Hi',
# 'Hello',
# 'I need your assistance regarding my order',
# 'Please, Provide me with your order id',
# 'I have a complaint.',
# 'Please elaborate, your concern',
# 'How long it will take to receive an order ?',
# 'An order takes 3-5 Business days to get delivered.',
# 'Okay Thanks',
# 'No Problem! Have a Good Day!'
# ])

trainer.train(
    "chatterbot.corpus.english"
)

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

#Change chrome driver path accordingly
chrome_driver = "chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

driver.get("https://web.whatsapp.com/")

input("Press anything after QR scan")
time.sleep(5)

names = ["Tanushree","Achu Jio", "Pallavi Bichupuriys"]
#message = "Android auto messaging bot here, " +  name + "!"

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
        # input_text = driver.find_element_by_xpath("//div[@class='_1Gy50'])[last()]").text # not working
        input_text = "wassup"
        output_text = chatter_bot_interaction(input_text)
        driver.find_element_by_xpath("//div[@title='Type a message']").send_keys(output_text)
        driver.find_element_by_xpath("//div[@title='Type a message']").send_keys(Keys.RETURN)


def chatter_bot_interaction(input_text):
    print("input : ", input_text)
    response = bot.get_response('what is the nature of social relationships to you?')

    print("Bot Response:", response)
    response = f"This is a ai bot generated message. Pay no heed. Message at {str(time.perf_counter())} ::: {response}"
    if(response):
        return response
    else :
        return f"fan bot is offline right now."

search_and_send_custom_messages(names)

