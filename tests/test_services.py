import pytest
from app.services import *

services = Services()

def test_docs():
    storyA = services.story_dict['A']
    assert storyA.text.split()[:1] == ["स्कूल"]
    storyB = services.story_dict['B']
    assert storyB.text.split()[:1] == ["मेरे"]
    storyC = services.story_dict['C']
    assert storyC.text.split()[:1] == ["आम"]


def test_show_docs():
    assert services.show_doc('A') == "Enjoy the story!"
    assert services.show_doc('B') == "Enjoy the story!"
    assert services.show_doc('C') == "Enjoy the story!"
    with pytest.raises(ValueError):
        services.show_doc('D')
        services.show_doc('1')


def test_show_dev_trans():
    assert services.show_dev_trans("पहला") == 'first'
    with pytest.raises(ValueError):
        services.show_dev_trans("tree")


def test_show_eng_trans():
    assert services.show_eng_trans("first") == 'पहला'
    with pytest.raises(ValueError):
        services.show_eng_trans("पहला")
