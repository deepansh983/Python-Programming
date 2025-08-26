#Write a program to print right aligned right-angled triangle
'''
        *
      * *
    * * *
  * * * *
* * * * *
'''
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()
print("-"*30)

for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end=" ")
    for k in range(i):
        print(i,end=" ")
    print()
print("-"*30)


for i in range(1, n+1):
    # spaces
    print("  "*(n-i), end="")
    # numbers in reverse order
    for j in range(i,0, -1):
        print(j, end=" ")
    print()   