# Program to check divisibility of number from 1 to 50 by 3 & 5:



i=1
while(i<=50):
        if(i%3==0 and i%5==0):
                print("FizzBuzz")
        elif(i%5==0):
                print("Buzz")
        elif(i%3==0):
                print("Fizz")
        else:
                print(i)
        i+=1
