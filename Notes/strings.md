
# [Format Strings](https://github.com/teacherubial/programming-2023-2024/blob/main/Notes/Strings.md#format-strings)

We can evaluate inside of strings using _f-strings_.  
To create an f-string, we put an `f` before the opening quote.

```python
fave_food = input("What's your favourite food? ")
print(f"Ooooooo, {fave_food} sounds good!")
```

# [String Methods](https://github.com/teacherubial/programming-2023-2024/blob/main/Notes/Strings.md#string-methods)

[[Objects#Methods|Methods]] are functions that we can use on [[Objects]].

String methods allow us to modify and work with strings.

Say for example, we want to make all characters of a string lowercase.

```python
mr_ubial_yelling = "PLEASE PUSH YOUR CHAIRS IN"

print(mr_ubial_yelling.lower())  # lowercases the letters
```

## [`.lower()`](https://github.com/teacherubial/programming-2023-2024/blob/main/Notes/Strings.md#lower)

The `.lower()` method takes a string and converts all UPPERCASE characters to lowercase.

We can use `.lower()` to help with [[Errors#Semantic Errors|errors]].

## [`.upper()`](https://github.com/teacherubial/programming-2023-2024/blob/main/Notes/Strings.md#upper)

The `.upper()` method converts all lowercase characters to uppercase in a string.

## [`.strip(str)`](https://github.com/teacherubial/programming-2023-2024/blob/main/Notes/Strings.md#stripstr)

The `.strip()` method **removes** characters from the beginning and end of the string.

```python
user_feeling = input("How are you feeling? ")

# "good" "Good" "GOOD" "GOOD!" "good." "good?" "!good!"
if user_feeling.lower().strip("!.,?") == "good":
	print("That's great!")
```

## [`.split(str) -> List`](https://github.com/teacherubial/programming-2023-2024/blob/main/Notes/Strings.md#splitstr---list)

The `.split()` method splits a string into a [[lists|list]], separating the string based on the characters you give it.

```python
grocery_str = "eggs milk cheese hotwheels"

grocery_list = grocery_str.split(" ")
```