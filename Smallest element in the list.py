# Program to find smallest number from a list:

ls = []
count = int(input(" Enter total count of numbers: "))

for i in range(count):
    number = int(input(" Enter Number"))
    ls.append(number)
print(" Smallest element in the list is: ", min(ls))
