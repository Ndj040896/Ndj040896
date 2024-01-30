# Program to check whether number given is perfect number or not:

 # A perfect number is a positive integer that is equal to the sum of its positive divisors,
        #excluding the number itself.
 #For instance, 6 has divisors 1, 2 and 3, and 1 + 2 + 3 = 6, so 6 is a perfect number. 
 # also numbers like 6,28,128, 496,525.....


n = int(input(" Enter any Number: "))
i = 1
sum = 0

while(i < n):
    if(n % i == 0):
        sum = sum + i
    i = i + 1   
if (sum == n):
    print(" Entered number %d is a Perfect number" %n)
else:
    print(" Entered number %d is not a Perfect number" %n)
