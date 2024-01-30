# Program to add 2 dictionaries:

di1 = {1:10,2:20,3:45,4:36}
di2 = {5:42,6:33,7:14,3:39}
di3 = {}
li1 = []
li2 = []

for i in di1:
        li1.append(i)

for j in di2:
        li2.append(j)
        
for i in range(len(li2)):
        di3[li1[i]+li2[i]]=di1[li1[i]]+di2[li2[i]]
        
print(di3)
