#Continue Satement Example:


i=0
str1 = " python"
while i<len(str1):
    if str1[i] == 'p' or str1[i]=='n':
     i+=1
     continue
    print('Current Letter: ', str1[i])
    i+= 1
