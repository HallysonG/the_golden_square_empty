import pytest
from lib.password_checker import *

def test_password_checker_valid():
    passwordchecker = PasswordChecker()
    result = passwordchecker.check("12345678")
    assert result == True

def test_password_check_error():
    passwordchecker = PasswordChecker()
    with pytest.raises(Exception) as e:
        result = passwordchecker.check("1234567")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

    