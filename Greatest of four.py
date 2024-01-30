# Program to chech greatest among four numbers:

a = int(input("Enter 1st Number : "))
b = int(input("Enter 2nd Number : "))
c = int(input("Enter 3rd Number : "))
d = int(input("Enter 4th Number : "))

if(a>b):
        if(a>c):
                print("A is Greatest.")
        elif(a>d):
                print("A is Greatest.")
        else:
             print("D is Greatest.")
            
elif(b>c):
        if(b>d):
             print("B is Greatest.")
        else:
             print("D is Greatest")
             
elif(c>d):
          print("C is Greatest.")

else:
     print(" D is Greatest.")
