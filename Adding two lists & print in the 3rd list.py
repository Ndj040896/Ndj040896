# Program to add 2 given list & print the result in a new list:

li1 = [12,10,45,30]
li2 = [15,16,17,12,10]
li3 = []
'''
li3 = [sum(i) for i in zip(li1, li2)]


print("Resulting List is: ", li3)
'''

if(len(li1)==len(li2)):
        for i in range(len(li1)):
                li3.append(li1[i]+li2[i])
                
if(len(li2)>len(li1)):
        count=0
        for i in range(len(li1)):
                li3.append(li1[i]+li2[i])
                count+=1
        for j in range(count,len(li2)):
                li3.append(li2[j])                

print(li3)
