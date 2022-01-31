from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from chatterbot import ChatBot
import time


def stripper(s): # Stripper function for removing last line

    try:
        return s[:s.rfind('\n')] # Return the message after removing last line

    except Exception as e:
        print("Exception occured")
        print(e)

def getQuery(query):
    try:
        user_input = query

        bot_response = bot.get_response(user_input)

        return bot_response

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except Exception as e:
        print("Exception occured")
        print(e)    


def main():
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")

    input("Press anything after QR scan")
    time.sleep(5)

    names="Tanushree"
    message = "Android auto messaging bot here, " +  names + "!"

    try:
        driver.find_element_by_xpath("//div[@role='textbox']").click() # Click on search button

        return
        driver.find_element_by_xpath("//div[@id='side']/div/div/label/input").clear()
        driver.find_element_by_xpath("//div[@id='side']/div/div/label/input").send_keys("Cute Camillus") #Type contact name
        time.sleep(5)
        driver.find_element_by_xpath("//div[2]/div[2]/div/span/span").click() #Click open chat name
        time.sleep(5)


        lastmessage = driver.find_elements_by_xpath("//div[@class='FTBzM message-in']")
        range = len(lastmessage)
        last = lastmessage[range-1]
        lsmsg = last.text
        finalmsg = stripper(lsmsg)
        firstfinal = finalmsg # First received message

        message = str(getQuery(finalmsg))
        message = "Yo this is a bot!"

        #con.clear()
        con = driver.find_element_by_xpath("//div[@id='main']/footer/div/div[2]/div/div[2]") #Find the reply box
        con.click() #Click the reply box
        con.send_keys(message) #type in the reply box
        con.send_keys(Keys.RETURN) #hit enter
    
    except Exception as e:
        print("An Error occured!")
        print(e)

if __name__ == '__main__':

    # chatbot = ChatBot('Adithyan AK')

    # bot = ChatBot(
    #     'Default Response Example Bot',
    #     storage_adapter='chatterbot.storage.SQLStorageAdapter',
    #     logic_adapters=[
    #         {
    #             'import_path': 'chatterbot.logic.BestMatch'
    #         },
    #         {
    #             'import_path': 'chatterbot.logic.BestMatch',
    #             'threshold': 0.90,
    #             'default_response': 'I am sorry, but I do not understand.'
    #         }
    #     ],
    #     trainer='chatterbot.trainers.ListTrainer'
    # )

    main()
