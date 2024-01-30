# Program to check year is a leap year or not:

yr = int(input("Enter year to check : "))

if(yr % 4==0 and yr % 100!=0 or yr% 400==0):
   print("The year is a leap year!")
else:
   print("The year isn't a leap year!")
