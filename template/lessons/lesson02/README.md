Lesson 02 – Lists, Tuples and Dictionaries
Write these functions in `solution.py`.

## Part 1. Lists (`list`)

1. `list_stats(numbers)` – takes a list of numbers (for example, 10 numbers) and prints the largest value, the smallest value and the sum of all elements (in this order). Print only these three numbers, with no other digits.
2. `reverse_names()` – read 5 names (`input()`), store them in a list and print them in reverse order.
3. Shopping list:
   - `add_item(shopping_list, item)` – adds a new item to the end of the given list (the list is changed in place).
   - `remove_item(shopping_list, item)` – removes the item from the list. If the item is not in the list, the program must not crash and the list stays unchanged.
   - `show_list(shopping_list)` – prints the whole list, with the items in their order.

## Part 2. Tuples (`tuple`) and dictionaries (`dict`)

4. `print_first_last(cities)` – takes a tuple of city names (for example, three cities) and prints only the first and the last elements.
5. A dictionary about a person:
   - `create_person(name, age, city)` – returns a dictionary with the keys `"name"`, `"age"` and `"city"`.
   - `show_person(person)` – takes such a dictionary and prints the person's name, age and city.
6. Phone book (a dictionary where the key is the name and the value is the phone number):
   - `add_contact(book, name, phone)` – adds a new contact to the given dictionary (the dictionary is changed in place).
   - `find_phone(book, name)` – returns the phone number for the given name, or `None` if there is no such contact.
   - `show_contacts(book)` – prints all contacts: the name and the phone number.

Check your work: `cd lessons/lesson02 && pytest -v`
