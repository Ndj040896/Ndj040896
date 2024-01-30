#  Program to count occurrence of a character in a String

string = "Hello"
char = 'l'

a = 0
for i in range(len(string)):
    if(string[i] == char):
        a = a + 1

print(" Total Number of Times ", char, "  Occurrs = " , a)
