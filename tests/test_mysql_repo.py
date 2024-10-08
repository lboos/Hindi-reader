import pytest
import db.mysql_repo

# Instantiate a MysqlRepository object to use for the queries
repo = db.mysql_repo.MysqlRepository()

def test_load_lexicon():
    lexicon = repo.load_lexicon()
    assert len(lexicon) >= 5

def test_dev_query():
    assert repo.dev_query("पहला") == [(2, 'पहला', None, 'first', None)]
    with pytest.raises(ValueError):
        repo.dev_query("tree")
    # assert repo.dev_query("tree") == []

def test_eng_query():
    # assert repo.eng_query("पहला") == []
    assert repo.eng_query("tree") == [(8, 'पेड़', None, 'tree', None)]
    with pytest.raises(ValueError):
        repo.eng_query("पहला")

def test_dev_gloss():
    gloss = repo.dev_gloss()
    assert len(gloss) >= 5
    assert "स्कूल" in gloss
    assert "पहला" in gloss
    assert 'tree' not in gloss

def test_eng_gloss():
    gloss = repo.eng_gloss()
    assert len(gloss) >= 5
    assert "school" in gloss
    assert "tree" in gloss
    assert 'पहला' not in gloss

# def test_add_term():
#     assert repo.add_term('हम', 'we') == True
#     assert repo.add_term('माँ', 'mother') == True

# def test_query():
#     assert (1, 'स्कूल', None, 'school', None) in repo.query_db("SELECT * FROM hindi_lexicon")
#     assert (3, 'दन', None, 'day', None) in repo.query_db("SELECT * FROM hindi_lexicon")
#     assert repo.query_db("SELECT * FROM hindi_lexicon WHERE dev = 'पहला'")[0][3] == 'first'
#     assert repo.query_db("SELECT * FROM hindi_lexicon WHERE dev = 'आम'")[0][3] == 'mango'
#     assert repo.query_db("SELECT * FROM hindi_lexicon WHERE word_eng = 'my'")[0][1] == 'मेरे'
