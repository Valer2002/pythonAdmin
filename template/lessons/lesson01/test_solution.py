import random
import re

from solution import (
    calculator,
    check_age,
    greet,
    guess_number,
    introduce,
    is_even,
    math_operations,
    multiples_of_five,
    sign_of_number,
    square,
    sum_to_n,
)


def fake_input(inputs, on_call=None):
    answers = iter(inputs)

    def _input(prompt=""):
        if on_call:
            on_call()
        try:
            return next(answers)
        except StopIteration:
            raise AssertionError("The program asked for more input than expected")

    return _input


def numbers_in(text):
    return {float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", text)}


def run(monkeypatch, capsys, func, inputs):
    monkeypatch.setattr("builtins.input", fake_input(inputs))
    func()
    return capsys.readouterr().out


# ---------- Part 1: variables ----------

def test_introduce_shows_name(monkeypatch, capsys):
    out = run(monkeypatch, capsys, introduce, ["Anna", "25", "Yerevan"])
    assert "Anna" in out, "the greeting should contain the name"


def test_introduce_shows_age(monkeypatch, capsys):
    out = run(monkeypatch, capsys, introduce, ["Anna", "25", "Yerevan"])
    assert "25" in out, "the greeting should contain the age"


def test_introduce_shows_city(monkeypatch, capsys):
    out = run(monkeypatch, capsys, introduce, ["Anna", "25", "Yerevan"])
    assert "Yerevan" in out, "the greeting should contain the city"


def test_math_positive(monkeypatch, capsys):
    out = run(monkeypatch, capsys, math_operations, ["10", "4"])
    nums = numbers_in(out)
    assert 14 in nums, "sum of 10 and 4 should be 14"
    assert 6 in nums, "difference of 10 and 4 should be 6"
    assert 40 in nums, "product of 10 and 4 should be 40"
    assert 2.5 in nums, "quotient of 10 and 4 should be 2.5"


def test_math_negative(monkeypatch, capsys):
    out = run(monkeypatch, capsys, math_operations, ["-6", "4"])
    nums = numbers_in(out)
    assert -2 in nums, "sum of -6 and 4 should be -2"
    assert -10 in nums, "difference of -6 and 4 should be -10"
    assert -24 in nums, "product of -6 and 4 should be -24"
    assert -1.5 in nums, "quotient of -6 and 4 should be -1.5"


def test_math_decimals(monkeypatch, capsys):
    out = run(monkeypatch, capsys, math_operations, ["2.5", "0.5"])
    nums = numbers_in(out)
    assert 3 in nums, "sum of 2.5 and 0.5 should be 3"
    assert 2 in nums, "difference of 2.5 and 0.5 should be 2"
    assert 1.25 in nums, "product of 2.5 and 0.5 should be 1.25"
    assert 5 in nums, "quotient of 2.5 and 0.5 should be 5"


# ---------- Part 2: conditionals ----------

def test_age_minor(monkeypatch, capsys):
    out = run(monkeypatch, capsys, check_age, ["17"]).lower()
    assert "minor" in out, '17 should be reported as "minor"'
    assert "adult" not in out, "17 is not an adult"


def test_age_adult_boundary(monkeypatch, capsys):
    out = run(monkeypatch, capsys, check_age, ["18"]).lower()
    assert "adult" in out, '18 should be reported as "adult"'
    assert "minor" not in out, "18 is already an adult"


def test_age_adult(monkeypatch, capsys):
    out = run(monkeypatch, capsys, check_age, ["40"]).lower()
    assert "adult" in out, '40 should be reported as "adult"'
    assert "minor" not in out, "40 is not a minor"


def test_sign_positive(monkeypatch, capsys):
    out = run(monkeypatch, capsys, sign_of_number, ["5"]).lower()
    assert "positive" in out, '5 should be "positive"'
    assert "negative" not in out, "5 is not negative"


def test_sign_negative(monkeypatch, capsys):
    out = run(monkeypatch, capsys, sign_of_number, ["-3"]).lower()
    assert "negative" in out, '-3 should be "negative"'
    assert "positive" not in out, "-3 is not positive"


def test_sign_zero(monkeypatch, capsys):
    out = run(monkeypatch, capsys, sign_of_number, ["0"]).lower()
    assert "zero" in out, '0 should be "zero"'
    assert "positive" not in out, "0 is not positive"
    assert "negative" not in out, "0 is not negative"


def test_sign_decimals(monkeypatch, capsys):
    out = run(monkeypatch, capsys, sign_of_number, ["-0.5"]).lower()
    assert "negative" in out, '-0.5 should be "negative"'
    out = run(monkeypatch, capsys, sign_of_number, ["0.5"]).lower()
    assert "positive" in out, '0.5 should be "positive"'


def test_calculator_add(monkeypatch, capsys):
    out = run(monkeypatch, capsys, calculator, ["7", "2", "+"])
    assert 9 in numbers_in(out), "7 + 2 should give 9"


def test_calculator_subtract(monkeypatch, capsys):
    out = run(monkeypatch, capsys, calculator, ["7", "2", "-"])
    assert 5 in numbers_in(out), "7 - 2 should give 5"


def test_calculator_multiply(monkeypatch, capsys):
    out = run(monkeypatch, capsys, calculator, ["7", "2", "*"])
    assert 14 in numbers_in(out), "7 * 2 should give 14"


def test_calculator_divide(monkeypatch, capsys):
    out = run(monkeypatch, capsys, calculator, ["7", "2", "/"])
    assert 3.5 in numbers_in(out), "7 / 2 should give 3.5"


# ---------- Part 3: functions ----------

def test_greet_prints_name(capsys):
    greet("Anna")
    out = capsys.readouterr().out
    assert "Anna" in out, 'greet("Anna") should print a message containing the name'


def test_greet_prints_something(capsys):
    greet("Ben")
    out = capsys.readouterr().out
    assert out.strip() != "", "greet should print a message"
    assert "Ben" in out, 'greet("Ben") should print a message containing "Ben"'


def test_square_positive():
    assert square(4) == 16, "square(4) should return 16"


def test_square_negative():
    assert square(-3) == 9, "square(-3) should return 9"


def test_square_zero():
    assert square(0) == 0, "square(0) should return 0"


def test_is_even_true():
    assert is_even(4) is True, "is_even(4) should return True"


def test_is_even_false():
    assert is_even(7) is False, "is_even(7) should return False"


def test_is_even_zero():
    assert is_even(0) is True, "is_even(0) should return True"


def test_is_even_negative():
    assert is_even(-2) is True, "is_even(-2) should return True"
    assert is_even(-3) is False, "is_even(-3) should return False"


# ---------- Part 4: loops ----------

def test_multiples_of_five(capsys):
    multiples_of_five()
    out = capsys.readouterr().out
    printed = [int(x) for x in re.findall(r"\d+", out)]
    assert printed == list(range(5, 101, 5)), "should print 5, 10, 15, ..., 100 and nothing else"


def test_sum_to_n_ten(monkeypatch, capsys):
    out = run(monkeypatch, capsys, sum_to_n, ["10"])
    assert 55 in numbers_in(out), "sum of 1..10 should be 55"


def test_sum_to_n_hundred(monkeypatch, capsys):
    out = run(monkeypatch, capsys, sum_to_n, ["100"])
    assert 5050 in numbers_in(out), "sum of 1..100 should be 5050"


def test_guess_number_hints(monkeypatch, capsys):
    monkeypatch.setattr(random, "randint", lambda a, b: 42)
    outputs = []
    monkeypatch.setattr(
        "builtins.input",
        fake_input(["50", "30", "42"], on_call=lambda: outputs.append(capsys.readouterr().out)),
    )
    guess_number()
    outputs.append(capsys.readouterr().out)

    too_high = outputs[1].lower()
    too_low = outputs[2].lower()
    correct = outputs[3]
    assert "high" in too_high, 'guessing 50 when the number is 42 should say "high"'
    assert "low" not in too_high, 'guessing 50 when the number is 42 should not say "low"'
    assert "low" in too_low, 'guessing 30 when the number is 42 should say "low"'
    assert "high" not in too_low, 'guessing 30 when the number is 42 should not say "high"'
    assert correct.strip() != "", "a correct guess should print a congratulation message"


def test_guess_number_first_try(monkeypatch, capsys):
    monkeypatch.setattr(random, "randint", lambda a, b: 7)
    out = run(monkeypatch, capsys, guess_number, ["7"])
    assert out.strip() != "", "a correct guess should print a congratulation message"
    assert "high" not in out.lower() and "low" not in out.lower(), "a correct guess should not give a hint"
