from plates import is_valid

def test_is_valid_start():
    assert is_valid("AA") == True
    assert is_valid("bf") == True
    assert is_valid("34") == False
    assert is_valid("A3") == False
    assert is_valid("6D") == False

def test_is_valid_lenght():
    assert is_valid("") == False
    assert is_valid("A") == False
    assert is_valid("DD") == True
    assert is_valid("DDD") == True
    assert is_valid("DDDF") == True
    assert is_valid("DDDGG") == True
    assert is_valid("DDDGGT") == True
    assert is_valid("DDDHJYT") == False

def test_is_valid_num_position():
    assert is_valid("aaa222") == True
    assert is_valid("AA33A") == False
    assert is_valid("AA03A") == False

def test_is_valid_punctuation():
    assert is_valid("AA.") == False
    assert is_valid("AAg g") == False
    assert is_valid("AA33A") == False
