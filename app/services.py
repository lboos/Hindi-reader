import model.classes
import model.docs
import db.mysql_repo

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

    # USE CASE 2 Hindi Translation - user can input a Devanagari word and get English translation(s).
    def show_dev_trans(self, word:str) -> str:
        print("Enter a Hindi word for translation:")
        self.word = word
        if self.word not in self.repo.dev_gloss():
            raise ValueError("Please enter a valid word:")
        else:
            return self.repo.dev_query(self.word)[0][3]

    # (NEW) USE CASE 3 English Translation - user can input an English word and get Hindi translation(s).
    def show_eng_trans(self, word:str) -> str:
        print("Enter an English word for translation:")
        self.word = word
        if self.word not in self.repo.eng_gloss():
            raise ValueError("Please enter a valid word:")
        else:
            return self.repo.eng_query(self.word)[0][1]




