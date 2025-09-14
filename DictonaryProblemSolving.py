# Write a python program to sort a dictonary by value
a={"a":10,"b":5,"c":25,"d":11,"e":45}
a=sorted(a.values())
print(a)

print('-'*40)

# write a python script to print a dictonay where the key numbers are b/w 1-15 and the the values are the square of the key
b={}
for i in range(1,16):
    b[i]=i**2
print(b)

print('-'*40)

# Write a program to multiply all items in a dictionary
c={'a':2,'b':4,'c':5,'d':10}
product=1
for i in c:
    product*=c[i]
print(product)    

print('-'*40)

# Write a python program to sort a dictionary by key
d={5:'a',1:'b',4:'c',8:'d',11:'e'}
d=sorted(d.keys())
print(d)