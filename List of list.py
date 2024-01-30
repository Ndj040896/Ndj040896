# Program to cretae a list of list:
'''
li1 = [12,10,25,14,25,36,36,21,14]
li1 = []
a = 3
print(li)
for idx in range(0,a):
        li1.append(li[idx::a])
          
print("List of Lists: " + str(li1))
'''


# Program to add list of lists in a new list:

li1 =[[10,20,30],[15,25,35],[17,27,36]]
li2 =[[40,50,60],[25,35,45],[15,17,19]]
li3=[]
for i in range(len(li1)):
        li=[]
        for j in range(len(li1[i])):
                li.append(li1[i][j]+li2[i][j])

        li3.append(li)

print(li3)


