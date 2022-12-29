# Functions with outputs

def format_name(f_name, l_name):
    formatted_first_name = f_name.title()
    formatted_last_name = l_name.title()
    return(f"Formatted name: {formatted_first_name} {formatted_last_name}")
    # return function returns the output of the function

output = format_name("sudeep", "poudel")

print(output)


# Multiple return values

length = input("Enter the length:\n>> ")
breadth = input("Enter the breadth:\n>> ")

def permeter_calc(length, breadth):
    if length == "" or breadth == "":
        return "Invalid Input"
    else:
        perimeter = 2*( int(length) + int(breadth) )
        return perimeter

print(permeter_calc(length, breadth))

# Docstrings

def area_calc(length, breadth):
    """This is a function to calculate the area. This
    is an example fo the docstring."""
    area = int(length) * int(breadth)
    return area

print(area_calc(length, breadth))