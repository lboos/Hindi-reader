from db.repo import *
import mysql.connector


class MysqlRepository(Repository):

    def __init__(self):
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',  # When you run this on your machine change it to 'localhost'
            'port': '32000',  # When you run this on your machine change it to '32000'
            'database': 'hindi'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    # def query_db(self, query: str):
    #     self.cursor.execute(query)
    #     return list(self.cursor)

    # def quick_query_db(self, query: str):
    #     self.cursor.execute(f"SELECT * FROM hindi_lexicon WHERE dev = {query}")
    #     return list(self.cursor)

    def dev_query(self, query: str):
        try:
            self.cursor.execute("SELECT * FROM hindi_lexicon WHERE word_dev = %s", (query,))
            return self.cursor.fetchall()
        except:
            print("An error occurred!")

        # if self.val not in story_dict.keys():
        #     print("\n Please enter a valid story option (A, B, or C):")
        #     raise ValueError('Not a valid story option')

    def eng_query(self, query: str):
        try:
            # Use a tuple to pass the parameter
            self.cursor.execute("SELECT * FROM hindi_lexicon WHERE word_eng = %s", (query,))
            return self.cursor.fetchall()
        except:
            print("An error occurred!")

    # def add_term(self, hindi_word: str, english_word: str):
    #     self.cursor.execute(f"INSERT INTO hindi_lexicon (dev, word_eng) VALUES ('{hindi_word}', '{english_word}')")
    #     print("Entry created successfully")
    #     self.connection.commit()
    #     return True

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


# repo = db.mysql_repo.MysqlRepository()
#
# print(quick_query_db("पहला"))