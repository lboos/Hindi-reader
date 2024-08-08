from db.repo import *
import mysql.connector


class MysqlRepository(Repository):

    def __init__(self):
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'db',  # When you run this on your machine change it to 'localhost'
            'port': '3306',  # When you run this on your machine change it to '32000'
            'database': 'hindi'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def story_query(self, query: str):
        if query not in self.dev_gloss():
            raise ValueError('Not a valid Hindi word')
        try:
            self.cursor.execute("SELECT * FROM hindi_story WHERE id = %s", (query,))
            res = self.cursor.fetchall()
            # check if res is empty
            # if empty, return an empty dictionary
            # return {}
            # else save the result as a new dictionary and return that
            if res:
                return dict(res)
            else:
                return {}
        except:
            print("An error occurred!")


    def dev_query(self, query: str):
        if query not in self.dev_gloss():
            raise ValueError('Not a valid Hindi word')
        try:
            self.cursor.execute("SELECT * FROM hindi_lexicon WHERE word_dev = %s", (query,))
            return self.cursor.fetchall()
        except:
            print("An error occurred!")


    def dev_gloss(self):
        try:
            self.cursor.execute("SELECT word_dev FROM hindi_lexicon")
            res = self.cursor.fetchall()
            gloss_list = []
            for el in res:
                gloss_list.append(el[0])
            return gloss_list
        except:
            print("An error occurred!")


    def eng_query(self, query: str):
        if query not in self.eng_gloss():
            raise ValueError('Not a valid English word')
        try:
            # Use a tuple to pass the parameter
            self.cursor.execute("SELECT * FROM hindi_lexicon WHERE word_eng = %s", (query,))
            return self.cursor.fetchall()
        except:
            print("An error occurred!")


    def eng_gloss(self):
        try:
            self.cursor.execute("SELECT word_eng FROM hindi_lexicon")
            res = self.cursor.fetchall()
            gloss_list = []
            for el in res:
                gloss_list.append(el[0])
            return gloss_list
        except:
            print("An error occurred!")


    def load_lexicon(self) -> list:
        sql = 'SELECT * FROM hindi_lexicon'
        self.cursor.execute(sql)
        entries = [{'id': id,
                    'word-Devanagari': word_dev,
                    'pos': pos,
                    'word-English': word_eng,
                    'definition': definition,
                    } for (id, word_dev, pos, word_eng, definition) in self.cursor]
        return entries


    # def add_term(self, hindi_word: str, english_word: str):
    #     self.cursor.execute(f"INSERT INTO hindi_lexicon (dev, word_eng) VALUES ('{hindi_word}', '{english_word}')")
    #     print("Entry created successfully")
    #     self.connection.commit()
    #     return True


    # def query_db(self, query: str):
    #     self.cursor.execute(query)
    #     return list(self.cursor)