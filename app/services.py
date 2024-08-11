import model.classes
import model.docs
from db.mysql_repo import MysqlRepository
from model.docs import HindiDoc
from model.docs import Word
from model.enums import PartOfSpeech



class Services:

    def __init__(self):
        # self.repo = db.mysql_repo.MysqlRepository()
        self.docs = model.docs
        self.story_dict = model.docs.story_dict
        self.repo = MysqlRepository()

    # Old non-db code
    # USE CASE 1 Hindi texts - user can choose a document in Devanagari to read.
    # def show_doc(self, val):
    #     hindi_doc = HindiDoc('', 'Not a valid story option', 'Please enter A, B, or C.')
    #     if val in self.story_dict.keys():
    #         hindi_doc = self.story_dict[val]
    #     # return HindiDoc object as json data
    #     return hindi_doc.data

    # USE CASE 1 Hindi Translation - user can input a Devanagari word and get English translation(s).
    def show_doc_db(self, val):
        story_tuple = self.repo.story_query(val)
        if len(story_tuple) == 0:
            hindi_doc = HindiDoc('', 'Not a valid story option', 'Please enter A, B, or C.')
        else:
            hindi_doc = HindiDoc(story_tuple[0], story_tuple[1], story_tuple[2])
        return hindi_doc.data

    # Old non-api code
    # # USE CASE 1 Hindi texts - user can choose a document in Devanagari to read.
    # def show_doc(self, val: str) -> str:
    #     print("Hindi Stories:")
    #     for key in self.story_dict.keys():
    #         print(f"{key}. {self.story_dict[key].title}")
    #     # print("Choose a story to read by entering A, B, or C:\n")
    #     self.val = val
    #     if self.val not in self.story_dict.keys():
    #         raise ValueError('Not a valid story option')
    #     else:
    #         print(self.story_dict[self.val], "\n")
    #     return "Enjoy the story!"


    # Still trying to get this to work
    # USE CASE 2 Hindi Translation - user can input a Devanagari word and get English translation(s).
    def show_dev_trans(self, word):
        word_tuple = self.repo.dev_query(word)
        if len(word_tuple) == 0:
            word_res = Word('', PartOfSpeech.NOUN, 'Not a valid word option', '')
        else:
            word_res = Word(word_tuple[0], word_tuple[1], word_tuple[2], word_tuple[3])
        return word_res


    # (NEW) USE CASE 3 English Translation - user can input an English word and get Hindi translation(s).
    # def show_eng_trans(self, word:str) -> str:
    #     print("Enter an English word for translation:")
    #     self.word = word
    #     if self.word not in self.repo.eng_gloss():
    #         raise ValueError("Please enter a valid word:")
    #     else:
    #         return self.repo.eng_query(self.word)[0][1]




