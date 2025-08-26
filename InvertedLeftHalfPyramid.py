# Write a program to print inverted left aligned right angle triangle
'''
1 1 1 1 1      * * * * *       5 4 3 2 1
2 2 2 2        * * * *         5 4 3 2
3 3 3          * * *           5 4 3
4 4            * *             5 4
5              *               5

'''
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):          #rows   1 to n+1 rows
    for j in range(n+1,i,-1):   #columns
        print(i,end=" ")
    print()
print("-"*30)

for i in range(1,n+1):
    for j in range(n+1,i,-1):
        print("*",end=" ")
    print()
print("-"*30)

for i in range(0,n):
    for j in range(n,i,-1):
        print(j,end=" ")
    print()    