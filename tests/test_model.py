import pytest
from model.classes import *

def test_HindiDoc():
    doc = HindiDoc("T", "ये टेस्ट हे")
    assert doc.id == "T"
    assert doc.text == "ये टेस्ट हे"
    print(doc)

def test_Word():
    word = Word("बिल्ली", "NOUN", "cat",
                definition = "शेर, चीते आदि की जाति का परंतु उनसे छोटा एक पशु जो प्रायः घरों में रहता है और पाला जाता है")
    for key in vars(word).keys():
        assert type(vars(word)[key]) == str
    assert word.dev == "बिल्ली"
    assert word.pos == "NOUN"
    assert word.eng == "cat"
    assert word.definition == "शेर, चीते आदि की जाति का परंतु उनसे छोटा एक पशु जो प्रायः घरों में रहता है और पाला जाता है"
    print(word)