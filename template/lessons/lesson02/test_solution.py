from solution import count_vowels, only_positive, total


def test_total():
    assert total([1, 2, 3]) == 6, "total([1, 2, 3]) should return 6"


def test_total_empty():
    assert total([]) == 0, "total([]) should return 0"


def test_only_positive():
    assert only_positive([-2, 0, 3, 5]) == [3, 5], "only_positive([-2, 0, 3, 5]) should be [3, 5]"


def test_count_vowels():
    assert count_vowels("Hello World") == 3, 'count_vowels("Hello World") should return 3'


def test_count_vowels_uppercase():
    assert count_vowels("AEIOU") == 5, 'count_vowels("AEIOU") should return 5'
