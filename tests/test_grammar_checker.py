from lib.grammar_checker import *

def test_correct_grammar_check():
    result = grammar_checker("Hello!")
    assert result == "This looks like it's grammatically correct!"

def test_wrong_grammar_check():
    result = grammar_checker("hdjkfhadkj")
    assert result == "This doesn't look like it's grammatically correct!"