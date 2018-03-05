from chatterbot import ChatBot
import time
# import logging
import speech_recognition as sr

# This turns on logs in terminal (Quite distracting)
# logging.basicConfig(level=logging.INFO)

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
query_answer = input("Please specify whether you want to type(1) or talk(2): ")
if (query_answer == "2"):
    r = sr.Recognizer()
    m = sr.Microphone()
    print("A moment of silence, please...")
    with m as source:
        r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    with sr.Microphone() as source:
        print("Speech recognition will begin in 3 second.")
        time.sleep(3)
        print("You may speak!")
        while True:
            audio = r.listen(source)
            try:
                item = r.recognize_google(audio)
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Can't talk with servers right now; {0}".format(e))
            if "end connection" in str(item):
                print("Very well, ending connection to Construct")
                time.sleep(2)
                exit()
            else:
                print(chatbot.get_response("" + item))
                time.sleep(2)
else:
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
