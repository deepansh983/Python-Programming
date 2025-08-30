a="Abhinav is Watching web series on netflix"
b="Rajat Is Walking On The Street"
print(a)

#To find the length of a string---Length Function
print(len(a))

#TO find the number of times a character is occuring
print(a.count("a"))

# To convert each case into upper case
print(a.upper())

# To convert each letterinto lower case
print(a.lower())

# to find the index of any character
print(a.index("a"))
print(a.index("a",5,25))

# to convert the first letter to capital
print(a.capitalize())

# to convert string into lower case
print(b.casefold())

# to find the index number of character
print(a.find("i"))
print(a.find("b",1,25))

# to write variables inside a string---- format method
name="John"
age=34
c="my name is {} and my age is {}"
print(c.format(name,age))

# it fills the given characters and centralizes a string, spaces is default ,but we can also fill any number,letter or charcters in place of spaces
print(name.center(20))  
print(name.center(20,"*"))    