import pytest

from app.hindi_reader import *


def test_docs():
    story = story_dict['A']
    assert story.split()[:1] == ["स्कूल"]
    story = story_dict['B']
    assert story.split()[:1] == ["मेरे"]
    story = story_dict['C']
    assert story.split()[:1] == ["आम"]

def test_hindi_doc():
    assert hindi_doc()

def test_show_docs():
    assert hindi_doc().show_docs('A') == 'test'
    assert hindi_doc().show_docs('B') == 'test'
    assert hindi_doc().show_docs('C') == 'test'
    with pytest.raises(ValueError):
        hindi_doc().show_docs('D')
        hindi_doc().show_docs('1')
    # assert hindi_doc().show_docs('D') == 'error'
    # assert hindi_doc().show_docs('1') == 'error'

def test_dict():
    assert hindi_dict().trans['दन'] == 'day'
    assert hindi_dict().trans['पेड़'] == 'tree'

def test_show_trans():
    assert hindi_dict().show_trans('स्कूल') == 'school'
    assert hindi_dict().show_trans('आम') == 'mango'
    assert hindi_dict().show_trans('पेड़') == 'tree'
    assert hindi_dict().show_trans('मुदित') == 'error'

