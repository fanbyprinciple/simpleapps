#supress all warnings
import warnings
warnings.filterwarnings("ignore")

from chatterbot import ChatBot
#bot = ChatBot('fan')

bot = ChatBot(
        'Default Response Example Bot',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch'
            },
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'threshold': 0.90,
                'default_response': 'I am sorry, but I do not understand.'
            }
        ],
        trainer='chatterbot.trainers.ListTrainer'
    )

#import ListTrainer
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

trainer.train(
    "chatterbot.corpus.english"
)

trainer.train([
'Hi',
'Hello',
'I need your assistance regarding my order',
'Please, Provide me with your order id',
'I have a complaint.',
'Please elaborate, your concern',
'How long it will take to receive an order ?',
'An order takes 3-5 Business days to get delivered.',
'Okay Thanks',
'No Problem! Have a Good Day!'
])



while(1):
    input_text = input("you: ")
    response = bot.get_response(input_text)
    print("fanbot: ", response)

# not working properly at all.