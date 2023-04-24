from lib.string_builder import *

def test_string_builder_length():
    stringbuilder = StringBuilder()
    stringbuilder.add("hello")
    result = stringbuilder.size()
    assert result == 5
    


def test_string_builder_text():
    stringbuilder = StringBuilder()
    stringbuilder.add("hello")
    result = stringbuilder.output()
    assert result == "hello"