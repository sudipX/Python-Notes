#Data Types

#String -> Anything inside single and double quotation marks
string_data = "This is a string"
print(string_data)

#Subscripting
first_character_of_string_data = string_data[0]
second_character_of_string_data = string_data[1]
last_character_of_string_data = string_data[15]
print(first_character_of_string_data)
print(second_character_of_string_data)
print(last_character_of_string_data)

#Concatenating
string_concat_data = "123" + "456"
print(string_concat_data)

#Integer -> Whole numbers (numbers without any decimal places)
integer_data = 22
print(integer_data * 5)

#Large Integers
print(1_81_181)

#Float -> Floating point numbers
pi = 3.14159

#Boolean -> Two possible values
boolean_data = True
boolean_data = False

#Type Checking & Conversion/Casting

#checking the data type
print(type(pi))
print(type(integer_data))

#Converting one data type to other
string_concat_data_to_int = int(string_concat_data)
print(type(string_concat_data_to_int))

#Mathematical operators in python
print(3 + 5) # -> Sum
print(3 - 5) # -> Subtraction
print(3 * 5) # -> Multiplication
print(6 / 3) # -> Division : Division always result in float data type in python
print(4 ** 3) # -> Raising the power 

# Priority
# PEMDAS
# P : Parentheses ()
# E : Exponents  **
# M : Multiplication *
# D : Division /
# A : Addition +
# S : Subtraction -

# Rounding Off
calculation = 8 / 3
print(round(calculation)) # round into whole number 
print(round(calculation, 2)) # rounding off to two decimal places

# Floor division
floor_calculation = 8 // 3 # floor division gives integer output rather than float
print(floor_calculation)
print(type(floor_calculation))

# F-Strings -> Converts all the data to string data type
age = 18
height = 2.5
isHandsome = True
print(f"Sudeep is {age} years old. His height is {height} and he is handsome which is {isHandsome}.")