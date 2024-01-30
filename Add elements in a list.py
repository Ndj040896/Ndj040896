# Program to add elements in a list:

ls = []
n = int(input('Enter total count of numbers: '))

for i in range(n):
    numbers = int(input("Number"))
    ls.append(numbers)
print("Sum of elements in given list is :", sum(ls))

