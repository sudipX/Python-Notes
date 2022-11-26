# For Loops

# Looping through lists
names = ["Sudeep", "Anish", "Kiran"]

for i in names: # Takes list of names and assign variable i to each of the item in the list
    print(i)
    print(i+" is a boy.")

# sum function -> gives sum of items in the list
li = [1,2,3,4,5]
print(sum(li))

# max function -> gives minimum value from the list
li2 = [78, 65, 89, 86, 55, 91, 64, 89]
print(max(li2))

# min function -> gives minimum value from the list
print(min(li2))

# For Loops With Range
# for n in range(x, y):
#     print(n)
# -> x is inclusive
# -> y is exclusive

for number in range(1, 100):
    print(number)

# Stepping through various sizes
# for n in range(x, y, z):
#     print(n)
# -> x is inclusive
# -> y is exclusive
# -> z is the step number

for number in range(1, 100, 3):
    print(number)

# Sum of numbers from 1 to 100
sum = 0
for n in range (1, 101):
    sum+=n
print(sum)