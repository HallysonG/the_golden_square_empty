from lib.gratitudes import *

def test_gratitudes1():
    gratitudes = Gratitudes()
    gratitudes.add("SNT")
    result = gratitudes.format()
    assert result == "Be grateful for: SNT"

def test_gratitudes2():
    gratitudes = Gratitudes()
    gratitudes.add("SNT")
    gratitudes.add("house")
    result = gratitudes.format()
    assert result == "Be grateful for: SNT, house"

def test_gratitudes0():
    gratitudes = Gratitudes()
    gratitudes.add("")
    result = gratitudes.format()
    assert result == "Be grateful for: "
