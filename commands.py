import subprocess
import os

class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "yeah", "confirm"]
        self.cancel = ["no", "negative", "don't", "wait", "cancel", "dee"]

    def discover(self, text):
        if "what" in text and "your name" in text:
            if "my" in text:
                self.respond("You haven't told me your name yet.")
            else:
                self.respond("My name is Serah. How are you?")

    def respond(self, response):
        subprocess.call("say " + response, shell=True)