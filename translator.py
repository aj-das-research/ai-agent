from langdetect import detect
from deep_translator import GoogleTranslator

class Translator:
    def __init__(self):
        self.translator = GoogleTranslator()

    def detect_language(self, text):
        return detect(text)

    def translate_to_english(self, text):
        return self.translator.translate(text, target='en')
