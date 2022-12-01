# Functions and functions with input

def greet():
    print("Hello there !")
    print("How do you do ?")
    print("See ya!")

greet()

# Functions with inputs

def call_my_name(name):
    print(f"Hello {name}")

call_my_name("Sudeep")

# parameter is the name of the data that is being passed in -> name
# argument is the actual data that is being passed -> Sudeep


# Functions with multiple inputs

def information_printer(name, age, height, isHandsome):
    print(f"My name is {name}. I am {age} years old.")
    print(f"I am handsome which is {isHandsome}.")
    print(f"My height is {height} ft.")

information_printer("Sudeep", 18, 5.1, True)

# Keyword arguments -> pointing out the parameter
information_printer(age=22, name="Sudip", isHandsome=True, height=5.1)