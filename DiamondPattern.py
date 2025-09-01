#Write a program to print a diamond
n=int(input("Enter number of rows:"))
#1st half of diamond
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
#2nd half of diamond
for i in range(n-1,0,-1):
    for j in range(n,i,-1):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()                   