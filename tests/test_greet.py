from lib.greet import *

def test_greet():
    result = greet("string")
    assert result == "Hello, string!"

    