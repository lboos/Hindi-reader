import mysql.connector


class MysqlRepository:

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

    def close(self):
        self.cursor.close()
        self.connection.close()

    def query_db(self, query:str):
        self.cursor.execute(query)
        return list(self.cursor)

    def add_term(self, hindi_word:str, english_word:str):
        self.cursor.execute(f"INSERT INTO hindi_lexicon (word_dev, word_eng) VALUES ('{hindi_word}', '{english_word}')")
        print("Entry created successfully")
        return True

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

