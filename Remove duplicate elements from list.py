# Program to remove duplicate elements from a list:

li1 = [1,2,3,4,3,5,6,7,4,8]
li = []

for i in li1:
    if i not in li:
       li.append(i)
       
print(list(li))
