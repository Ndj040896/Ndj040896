# Program to remove an element from a specific index:

li = [2,3,4,5,6]
li1 =[]


ind = int(input("Enter index : "))
ele = int(input("Enter element to remove : "))

for i in range(ind):
       li1.append(li[i])

li1.remove(ele)

for j in range(ind,len(li)):
        li1.append(li[j])

print(li1)
