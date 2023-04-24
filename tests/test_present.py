import pytest
from lib.present import *

def test_unwrapping_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value) # <-- New code
    assert error_message == "No contents have been wrapped."

def test_wrapping_already_wrapped():
    present = Present()
    present.wrap(11)
    with pytest.raises(Exception) as e:
        present.wrap(33)
    error_message = str(e.value) # <-- New code
    assert error_message == "A contents has already been wrapped."
