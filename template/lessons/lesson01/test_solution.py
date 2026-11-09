from solution import add, greet, is_even


def test_add_positive():
    assert add(2, 3) == 5, "add(2, 3) should return 5"


def test_add_negative():
    assert add(-1, 1) == 0, "add(-1, 1) should return 0"


def test_is_even_true():
    assert is_even(4) is True, "is_even(4) should return True"


def test_is_even_false():
    assert is_even(7) is False, "is_even(7) should return False"


def test_greet():
    assert greet("Ann") == "Hello, Ann!", 'greet("Ann") should return "Hello, Ann!"'
