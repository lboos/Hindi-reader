from docs import *

class hindi_doc:

    def __init__(self):
        pass

    def show_docs(self, val:str) -> str:
        print("Hindi Stories:")
        print("A. First Day of School")
        print("B. My Friends")
        print("C. The Mango Tree")
        print("Choose a story to read by entering A, B, or C:\n")
        self.val = val
        if self.val not in story_dict.keys():
            print("\n Please enter a valid story option (A, B, or C):")
            return "error"
        else:
            print(story_dict[self.val], "\n")
        return "test"


class hindi_dict:

    def __init__(self):
        self.trans = {'स्कूल':'school', 'पहला' : 'first', 'दन': 'day', 'मेरे': 'my',
                      'दोत': 'friend or friends', 'आम' : 'mango', 'का' : 'possessive identifier',
                      'पेड़': 'tree'}
        pass

    def show_trans(self, word:str) -> str:
        print("Enter a Hindi word for translation:")
        self.word = word
        if self.word not in self.trans.keys():
            print("\n Please enter a valid word:")
            return "error"
        else:
            return self.trans[self.word]