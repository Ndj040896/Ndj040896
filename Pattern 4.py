# Program to print pattern :
                             # * * * * *
                             #   * * * *
                             #     * * *
                             #       * *
                             #         *

n = 5

for i in range( n, 0 , -1):
    for j in range(i-n,n-i):
        print(end=" ")
         
    for j in range(0,i):
        print("*", end=" ")
    print(" ")
