# Program to add common elements of 2 given lists:

li1 = [12,10,45,30]
li2 = [15,16,17,12,10]
li3 = []

for i in li1:
        if i in li2:
                li3.append(i+i)
        else:
                li3.append(i)


for i in li2:
        if i not in li1:
                li3.append(i)

        
print(li3)
