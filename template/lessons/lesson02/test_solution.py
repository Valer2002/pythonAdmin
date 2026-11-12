import re

from solution import (
    add_contact,
    add_item,
    create_person,
    find_phone,
    list_stats,
    print_first_last,
    remove_item,
    reverse_names,
    show_contacts,
    show_list,
    show_person,
)


def fake_input(inputs):
    answers = iter(inputs)

    def _input(prompt=""):
        try:
            return next(answers)
        except StopIteration:
            raise AssertionError("The program asked for more input than expected")

    return _input


def numbers_in_order(text):
    return [float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", text)]


def positions(text, items):
    for item in items:
        assert item in text, f"{item!r} should be printed"
    return [text.index(item) for item in items]


# ---------- Part 1: lists ----------

def test_list_stats_mixed(capsys):
    list_stats([3, 9, -2, 7, 15, 4, 0, 8, 11, 6])
    out = capsys.readouterr().out
    assert numbers_in_order(out) == [15, -2, 61], "should print max 15, min -2 and sum 61, in this order"


def test_list_stats_ascending(capsys):
    list_stats([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    out = capsys.readouterr().out
    assert numbers_in_order(out) == [100, 10, 550], "should print max 100, min 10 and sum 550, in this order"


def test_reverse_names(monkeypatch, capsys):
    names = ["Anna", "Ben", "Carl", "David", "Eva"]
    monkeypatch.setattr("builtins.input", fake_input(names))
    reverse_names()
    out = capsys.readouterr().out
    pos = positions(out, list(reversed(names)))
    assert pos == sorted(pos), "names should be printed in reverse order: Eva first, Anna last"


def test_reverse_names_asks_five_times(monkeypatch, capsys):
    answers = iter(["a1", "b2", "c3", "d4", "e5", "f6"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(answers))
    reverse_names()
    out = capsys.readouterr().out
    assert "f6" not in out, "the program should ask for exactly 5 names"
    assert next(answers) == "f6", "the program should not read more than 5 names"


def test_add_item():
    shopping = []
    add_item(shopping, "bread")
    add_item(shopping, "milk")
    assert shopping == ["bread", "milk"], "add_item should append the item to the end of the list"


def test_remove_item():
    shopping = ["bread", "milk", "eggs"]
    remove_item(shopping, "milk")
    assert shopping == ["bread", "eggs"], "remove_item should remove the item from the list"


def test_remove_missing_item():
    shopping = ["bread", "milk"]
    remove_item(shopping, "eggs")
    assert shopping == ["bread", "milk"], "removing a missing item should not change the list or crash"


def test_show_list(capsys):
    show_list(["bread", "milk", "eggs"])
    out = capsys.readouterr().out
    pos = positions(out, ["bread", "milk", "eggs"])
    assert pos == sorted(pos), "show_list should print all items in their order"


def test_show_empty_list_does_not_crash(capsys):
    show_list([])
    capsys.readouterr()


# ---------- Part 2: tuples and dictionaries ----------

def test_print_first_last(capsys):
    print_first_last(("Yerevan", "Gyumri", "Vanadzor"))
    out = capsys.readouterr().out
    assert "Yerevan" in out, "the first city should be printed"
    assert "Vanadzor" in out, "the last city should be printed"
    assert "Gyumri" not in out, "the middle city should not be printed"


def test_create_person():
    person = create_person("Anna", 25, "Yerevan")
    assert person == {"name": "Anna", "age": 25, "city": "Yerevan"}, \
        'create_person should return a dict with keys "name", "age", "city"'


def test_show_person(capsys):
    show_person({"name": "Anna", "age": 25, "city": "Yerevan"})
    out = capsys.readouterr().out
    assert "Anna" in out, "the name should be printed"
    assert "25" in out, "the age should be printed"
    assert "Yerevan" in out, "the city should be printed"


def test_add_contact():
    book = {}
    add_contact(book, "Anna", "077123456")
    add_contact(book, "Ben", "093654321")
    assert book == {"Anna": "077123456", "Ben": "093654321"}, \
        "add_contact should store name -> phone in the dictionary"


def test_find_phone():
    book = {"Anna": "077123456", "Ben": "093654321"}
    assert find_phone(book, "Ben") == "093654321", "find_phone should return the phone of the given name"


def test_find_phone_missing():
    book = {"Anna": "077123456"}
    assert find_phone(book, "Carl") is None, "find_phone should return None for an unknown name"


def test_show_contacts(capsys):
    show_contacts({"Anna": "077123456", "Ben": "093654321"})
    out = capsys.readouterr().out
    for text in ["Anna", "077123456", "Ben", "093654321"]:
        assert text in out, f"{text!r} should be printed"
