# Program to sort elements of a list in ascending order:

ls = []
n = int(input("Enter toatal count of elements: "))
i = 0
for i in range(i, n+1):
   numbers = int(input("Enter numbers: "))
   ls.append(numbers)

for i in range(n):
          for j in range(i+1, n):
              if(ls[i] > ls[j]):
                a = ls[i]
                ls[i] = ls[j]
                ls[j] = a

print("Elements in ascending order are: ",ls)
          
