from model.classes import *
from db.mysql_repo import *
import model.classes
import model.docs
import db.mysql_repo


# story_dict = {'A' : first_day_of_school, 'B': my_friends, 'C':the_mango_tree}

class Services:

    def __init__(self):
        self.repo = db.mysql_repo.MysqlRepository()
        self.docs = model.docs
        self.story_dict = model.docs.story_dict


    # USE CASE 1 Hindi texts - user can choose a document in Devanagari to read.
    def show_doc(self, val: str) -> str:
        print("Hindi Stories:")
        for key in self.story_dict.keys():
            print(f"{key}. {self.story_dict[key].title}")
        print("Choose a story to read by entering A, B, or C:\n")
        self.val = val
        if self.val not in self.story_dict.keys():
            raise ValueError('Not a valid story option')
        else:
            print(self.story_dict[self.val], "\n")
        return "Enjoy the story!"

    # USE CASE 2 Translation - user can input a Devanagari word from a document (possibly using copy/paste) and the output is English translation(s) of the word.
    def show_dev_trans(self, word:str) -> str:
        print("Enter a Hindi word for translation:")
        self.word = word
        try:
            return self.repo.dev_query(self.word)
        except:
            print("An error occurred!")






