from chatterbot import ChatBot
import time
# import logging
import speech_recognition as sr
import pyttsx3

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
query_answer = input(
    "Please specify whether you want to type(1) or talk(2) or experimental(3): ")
if (query_answer == "2"):
    r = sr.Recognizer()
    m = sr.Microphone()
    print("A moment of silence, please...")
    with m as source:
        r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    with sr.Microphone() as source:
        print("Speech recognition will begin in a moment.")
        engine = pyttsx3.init()
        engine.say('Hello there.')
        engine.runAndWait()
        print("You may speak!")
        while True:
            audio = r.listen(source)
            try:
                item = r.recognize_google(audio)
                print("You: " + item)
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Can't talk with servers right now; {0}".format(e))
            if "end connection" in str(item):
                print("Very well, ending connection to Construct")
                time.sleep(2)
                exit()
            else:
                response = chatbot.get_response("Chatbot: " + item)
                print(response)
                engine.say(response)
                engine.runAndWait()
                # time.sleep(2)
elif(query_answer == "3"):
    r = sr.Recognizer()
    m = sr.Microphone()
    print("A moment of silence, please...")
    with m as source:
        r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    with sr.Microphone() as source:
        print("Speech recognition will begin in a moment.")
        engine = pyttsx3.init()

        def speak(a):
            engine.say(a)
            engine.runAndWait()
            time.sleep(.5)

        def hear():
            audio = r.listen(source)
            try:
                item = r.recognize_google(audio)
                print("You: " + item)
                return(item)
            except sr.UnknownValueError:
                print("Could not understand audio")
                return ("Error")
            except sr.RequestError as e:
                print("Can't talk with servers right now; {0}".format(e))
                return ("Error b")

        # engine.say('Hello there.')
        # engine.runAndWait()
        time.sleep(.5)
        speak("My name is corinth!")
        nameTruth = False
        name = "you"
        while not nameTruth:
            speak("What is your name?")
            item = hear()
            prep = str("Your name is " + item + "? Is that correct?")
            speak(prep)
            item = hear()
            if item == "yes":
                nameTruth = True
                name = item
            else:
                speak("Sorry about that, let's try again.")
        prep = str("It is a pleasure to meet you" + name)
        speak(prep)
        prep = str("Now " + name + ". Please do not judge me too harshly. I am capable of many things given my training dataset is sufficent. I am currently relying on a suboptimal dataset of movie quotes circa 2003. Given a larger dataset I am certain I could master the english language, but for now I am what I am.")
        speak(prep)
        while True:
            audio = r.listen(source)
            # try:
            #     item = r.recognize_google(audio)
            #     print("You: " + item)
            # except sr.UnknownValueError:
            #     print("Could not understand audio")
            # except sr.RequestError as e:
            #     print("Can't talk with servers right now; {0}".format(e))
            if "end connection" in str(item):
                print("Very well, ending connection to Construct")
                time.sleep(2)
                exit()
            else:
                response = chatbot.get_response("Chatbot: " + item)
                print(response)
                engine.say(response)
                engine.runAndWait()
                # time.sleep(2)
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
