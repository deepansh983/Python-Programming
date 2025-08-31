#Write a program to get fibonacci series upto 10 numbers
first=0
second=1
n=int(input("Enter a number here:"))
if n==1:
    print(1)
else:
    print(first,second,end=" ")
    
    for i in range(2,n):
        result=first+second
        first=second
        second=result
        print(result,end=" ")
print()

# Alternate method
a, b = 0, 1

for i in range(n):   # loop 10 times
    print(a, end=" ") # print current number
    a, b = b, a + b   # update values
        