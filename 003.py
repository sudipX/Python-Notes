# Conditional Statements
print("Welcome to the rollercoaster!")
height = int(input("Enter your height in cm: \n"))

if height > 120:
    print("You can ride the rollercoaster.")
else:
    print("Sorry you have to grow taller before you can ride.")

# Comparison Operators
# > - Greater than
# < - Less than
# >= - Greater than or equal to
# <= - Less than or equal to
# == - Equal to

# Nested If and ELIF Statements
age = int(input("Enter your age:\n"))

if height >= 120:
    if age < 12:
        print("You need to pay $5.")
    elif age <= 18:
        print("You need to pay $7.")
    else:
        print("You need to pay $12.")
else:
    print("You are not eligible.")

# Multiple If Statements -> Checks all the possible if conditions
n = 0
status = int(input("Input your status: \n"))
if status < 10:
    n+= 10
    print(n)
if status < 20:
    n+= 20
    print(n)

# Logical operators
# and
# or
# not

