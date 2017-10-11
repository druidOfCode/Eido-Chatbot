from chatterbot import ChatBot
import time

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
#chatbot.train("chatterbot.corpus.english")

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
