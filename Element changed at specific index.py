# Program to change element at specific Index:

li = [ 1,2,4,5,6,7]
li1 =[]

print(li)

ind = int(input("Enter index : "))#1
ele = int(input("Enter element for insert : "))#27

for i in range(ind):
       li1.append(li[i])

li1.append(ele)

for j in range(ind,len(li)):
        li1.append(li[j])

print(li1)

