# Random Module
import random

# random whole numbers
random_integer = random.randint(1, 10)
print(random_integer) 

# random floating point number
random_float = random.random() # -> gives output between 0-1 but not 1
print(random_float)

# create random decimal number between 0 and 5
print(random_float * 5)

# Python Lists
fruits = ["Apple", "Mango", "Banana", "Grapes", "Orange"]

# pulling out data from list; use of index number
print(fruits[0]) # programmers start counting from zero

# Changing the items in the list
fruits[1] = "Mangoes"
print(fruits)

# Add and item at the end of the list
fruits.append("Avocado")
print(fruits)

# adding multiple items at the end of the list
fruits.extend(["Tomato", "Fig"])
print(fruits)

# Splitting string into list
str_input = "Hello,world."
str_to_list = str_input.split(",")
print(str_to_list)

# Random item from the list
print(random.choice(fruits))

# Nesting of lists
pro_languages = ["Java", "C", "C++", "Python", "Dart"]
languages = ["Nepali", "English", "French", "Russian"]

all_languages = [pro_languages, languages]
print(all_languages)
