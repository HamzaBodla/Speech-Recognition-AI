import os
import pyttsx3
from answer import Fetcher
from urllib.parse import quote

class Commander:
    def __init__(self):
        self.confirm = "yes"
        self.cancel = "no"

    def discover(self, text):
        if "what" in text and "your name" in text:
            self.respond("My name is Dravada, I am Hamza's Assistant")
            
        else:
            query = quote(text)
            f = Fetcher(f"https://www.google.co.uk/search?q={query}")
            answer = f.lookup()
            self.respond(answer)
            # self.respond("Sorry, I didnt catch that")

    def respond(self, response):
        print(response)
        engine = pyttsx3.init()
        engine.say(response)
        engine.runAndWait()


