# Program to remove items from set by value:

sets = {1, 2, 11, 6, 7, 4, 5, 6}
to_del = [2,11]

for elem in to_del:
    sets.discard(elem)

print('New Set is: ')
print(sets)
