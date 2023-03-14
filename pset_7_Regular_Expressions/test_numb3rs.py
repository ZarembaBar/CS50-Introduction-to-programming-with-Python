from numb3rs import validate


def test_validate_if_numbers_at_all_positions():
    assert validate("AAA.111.111.111") == False
    assert validate("111.AAA.111.111") == False
    assert validate("111.111.AAA.111") == False
    assert validate("111.111.111.AAA") == False
    assert validate("111.111.111.111") == True

def test_validate_if_numbers_in_right_range():
    assert validate("266.111.111.111") == False
    assert validate("111.266.111.111") == False
    assert validate("111.111.266.111") == False
    assert validate("111.111.111.266") == False

def test_validate_if_position_is_not_empty():
    assert validate(".111.111.111") == False
    assert validate("111..111.111") == False
    assert validate("111.111..111") == False
    assert validate("111.111.111.") == False
    assert validate("111. .111.111") == False
