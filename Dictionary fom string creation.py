# Program to create a dictionary from a string:

'''
str = 'w3resource'
d = {}

for ch in str:
    d[ch] = d.get(ch, 0) + 1
    
print(d)
'''

str = 'w3resource'
d = {}

for ch in str:
    count_char = str.count(ch)
    if count_char == 1:
        d[ch] = 1
    else:
        d[ch] = 1

print(d)
