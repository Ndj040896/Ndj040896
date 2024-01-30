# Program to print triangle pattern using * with for loop:


n = 5

for i in range(0,n+5,2): 
    for j in range(-3,n-i):
        print(end = " ")     
    for j in range(0, i+1): 
        print("*", end=' ')
    print("")
