import db.mysql_repo

# Instantiate a MysqlRepository object to use for the queries
repo = db.mysql_repo.MysqlRepository()


def test_query():
    assert (1, 'स्कूल', None, 'school', None) in repo.query_db("SELECT * FROM hindi_lexicon")
    assert (3, 'दन', None, 'day', None) in repo.query_db("SELECT * FROM hindi_lexicon")
    assert repo.query_db("SELECT * FROM hindi_lexicon WHERE word_dev = 'पहला'")[0][3] == 'first'
    assert repo.query_db("SELECT * FROM hindi_lexicon WHERE word_dev = 'आम'")[0][3] == 'mango'
    assert repo.query_db("SELECT * FROM hindi_lexicon WHERE word_eng = 'my'")[0][1] == 'मेरे'

def test_load_lexicon():
    lexicon = repo.load_lexicon()
    assert len(lexicon) >= 5

def test_add_term():
    assert repo.add_term('हम', 'we') == True
    assert repo.add_term('माँ', 'mother') == True