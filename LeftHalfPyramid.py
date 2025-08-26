#Write a program to print left aligned right-angle triangle pattern like this:
'''
 1               1              *
 1 2             2 2            * *
 1 2 3           3 3 3          * * *
 1 2 3 4         4 4 4 4        * * * *
 1 2 3 4 5       5 5 5 5 5      * * * * *
 '''
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):        #this loop is for rows    1 to n+1 rows
    for j in range(1,i+1):  #this loop is for columns   
        print(j,end=" ")
    print()
print("-"*30)

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
print("-"*30)

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()    