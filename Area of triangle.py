# Program to claculate area of triangle:

a = float(input("Enter first side of triangle:"))
b = float(input("Enter second side of triangle:"))
c = float(input("Enter third side of triangle:"))
s = (a + b + c) / 2
Area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(" The Area of a Triangle is %0.2f" %Area)
