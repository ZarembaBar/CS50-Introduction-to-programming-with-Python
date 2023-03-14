from twttr import shorten


def test_shorten():
    assert shorten("bartek") == "brtk"
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("12345") == "12345"
    assert shorten("@#$") == "@#$"
    assert shorten(",./") == ",./"
