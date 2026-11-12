Lesson 01 – Python Basics
Write these functions in `solution.py`. Functions that use `input()` and `print()` take no parameters.

## Part 1. Variables

1. `introduce()` – ask the user for their name, age and city (in this order), then print a nice greeting that contains all three values.
2. `math_operations()` – read two numbers `a` and `b` (in this order, they may be decimals), then print their sum, difference, product and quotient.

## Part 2. Conditionals and user input

3. `check_age()` – read the user's age. Print "minor" if the age is less than 18, otherwise print "adult" (18 is already an adult). The other word must not appear in the output.
4. `sign_of_number()` – read a number (it may be a decimal). Print "positive", "negative" or "zero". The other two words must not appear in the output.
5. `calculator()` – read the first number, the second number and the operation (`+`, `-`, `*`, `/`), in this order. Print the result of the operation.

## Part 3. Functions

6. `greet(name)` – takes a name and prints (`print`) a greeting message that contains this name.
7. `square(number)` – returns the square of the given number.
8. `is_even(number)` – returns `True` if the number is even, otherwise `False`.

## Part 4. Loops

9. `multiples_of_five()` – print all numbers from 1 to 100 that are divisible by 5. Print only the numbers (one per line or separated by spaces), with no other digits.
10. `sum_to_n()` – read a number `N` (`input()`), find the sum of all numbers from 1 to `N` and print it.
11. `guess_number()` – the "Guess the number" game. Choose the secret number with `random.randint(1, 100)` (write `import random` and call `random.randint`). The user guesses with `input()` until they get it right. After each guess:
    - if the guess is higher than the secret number, print a message containing the word "high" (and not "low"),
    - if it is lower, print a message containing the word "low" (and not "high"),
    - if it is correct, print a congratulation message and finish the game (do not call `input()` again).

Check your work: `cd lessons/lesson01 && pytest -v`
