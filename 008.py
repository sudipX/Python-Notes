# Dictionaries
#dictionary = {key : value}

# creating a dictionary
programming_dictionary = {
    "Bug" : "An error in a program that prevents the program from running as expected.",
    "Function" : "A piece of code that you can easily call over and over again.",
    "Loop" : "The action of doing something over and over again.",
    502 : 500+0+2 
}

# retrieving items from dictionary
# specify the key
print(programming_dictionary["Bug"])
print(programming_dictionary["Function"]) 
print(programming_dictionary["Loop"])
print(programming_dictionary[502])

# Adding new items to the dictionary
programming_dictionary["My_name"] = "Sudeep"
print(programming_dictionary)

# Editing an item in the dictionary
programming_dictionary[502] = "Five Hundred & Two"
print(programming_dictionary)

# Creating empty dictionary
my_information = {}

# Looping through the dictionary
for key in programming_dictionary:
    print(key) # gives keys not the values inside the keys
    print(programming_dictionary[key]) # gives values

# Wiping entire existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# Nesting Dictionary inside a Dictionary

travel_log = {
    "Nepal" : {
        "cities_visited" : ["Kathmandu", "Pokhara", "Bardibas"],
        "times_visited" : 100,
        "Review" : "Excellent"
    },
    "India" : {
        "cities_visited" : ["Delhi", "Banglore", "Sikkim"],
        "times_visited" : 2,
        "Review" : "Good"
    }
}

print(travel_log["Nepal"]["cities_visited"][1])

# Nesting Dictionary inside a List

new_travel_log = [
    {
        "country" : "Nepal",
        "cities_visited" : ["Kathmandu", "Pokhara", "Bardibas"],
        "times_visited" : 100,
        "Review" : "Excellent"
    },
    {
        "country" : "India",
        "cities_visited" : ["Delhi", "Banglore", "Sikkim"],
        "times_visited" : 2,
        "Review" : "Good"
    }
]

print(new_travel_log[1]["cities_visited"][0])