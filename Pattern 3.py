# Program to print the pattern: # 1
                                # 2 3
                                # 4 5 6
                                # 7 8 9 10
                                # 11 12 13 14 15

n = 1
stop = 2
r = 5 

for i in range(r):
    for col in range(1, stop):
        print(n, end=' ')
        n += 1
    print("")
    stop += 1
