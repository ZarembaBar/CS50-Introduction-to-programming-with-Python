from bank import value


def test_value_0():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("HeLLo, Bartek") == 0
    assert value("heLLo, Bartek") == 0


def test_value_20():
    assert value("How you doing?") == 20
    assert value("hi") == 20
    assert value("Hey") == 20


def test_value_100():
    assert value("What's happening") == 100
