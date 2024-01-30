# Program to sort a dictionary by value:

di2 = {5:42,6:33,7:14,3:39}
li =[]

for i in di2:
      li.append(di2[i])

li.sort()
c=0
for i in di2:
        di2[i] = li[c]
        c+=1
print(di2)
