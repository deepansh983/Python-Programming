A=["Ross","Rachel","Monica","Joe"]

# WAP to swap 1st and 4th element
A[0],A[3]=A[3],A[0]
print(A)
print("-"*40)

# WAP to add new value at second position
A.insert(1,"Jerry")
print(A)
print("-"*40)

# WAP to delete value from 3rd position
A.pop(2)
print(A)
print("-"*40)

B=[13,7,12,10]

# WAP to multiply all the number in the list
mul=1
for i in B:
    mul*=i
print(mul)
print("-"*40)

# WAP to get the largest  number from the list
B.sort()   #sort list in ascending order
print(B)
print("The largest value in the list is:",B[-1])
print("-"*40)

#alternate method
max=None
for i in B:
    if max is None or i>max:
        max=i
print(max)
print("-"*40)

# WAP to get the smallest number from the list
B.sort()   #sort list in ascending order
print(B)
print("The smallest value in the list is:",B[0])
print("-"*40)