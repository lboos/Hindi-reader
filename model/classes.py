from model.enums import *

class HindiDoc:

    def __init__(self, id: str, title: str, text: str):
        self.id = id
        self.title = title
        self.text = text
        # pass

    def __str__(self):
        return self.text

    @property
    def data(self):
        return {
            "id": self.id,
            "title": self.title,
            "text": self.text
        }

class Word:

    def __init__(self, dev: str, pos: PartOfSpeech, eng: str, definition: str):
        self.dev = dev
        self.pos = pos
        self.eng = eng
        self.definition = definition

    def __str__(self):
        return self.dev

    @property
    def data(self):
        return {
            "dev": self.dev,
            "pos": self.pos,
            "eng": self.eng,
            "definition": self.definition
        }

