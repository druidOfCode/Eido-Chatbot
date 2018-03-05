from chatterbot import ChatBot
import chatterbot
from settings import TWITTER
import time
import logging


# This turns on logs in terminal (Quite distracting)
# logging.basicConfig(level=logging.INFO)

# This is the twitter module, be sure to comment out the othe bot before using this!
# chatbot = ChatBot(
#    "TwitterBot",
#    logic_adapters=[
#        "chatterbot.logic.BestMatch"
#    ],
#    database="./twitter-database.db",
#    twitter_consumer_key=TWITTER["CONSUMER_KEY"],
#    twitter_consumer_secret=TWITTER["CONSUMER_SECRET"],
#    twitter_access_token_key=TWITTER["ACCESS_TOKEN"],
#    twitter_access_token_secret=TWITTER["ACCESS_TOKEN_SECRET"],
#    trainer="chatterbot.trainers.TwitterTrainer",
#)
# chatbot.train()


chatbot = ChatBot(
    'Eido',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database='./chat-database.sqlite3',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
)

# More training
chatbot.train("chatterbot.corpus.english.greetings")
chatbot.train("chatterbot.corpus.english.conversations")

# Get a response to an input statement
while True:
    item = input("Type Message: ")
    if "end connection" in str(item):
        print("Very well, ending connection to Construct")
        time.sleep(2)
        exit()
    else:
        print(chatbot.get_response("" + item))
        time.sleep(2)
