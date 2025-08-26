# 2)write a program to write first 20 number and their squared number    
print("First twenty number and their square number are:")
#Using for loop to take value from 1 to 20
for i in range(1,21):
    print(i,"=",i**2)

    #alternate method
    #print(i,end="=")
    #print(i**2,end="")
    #print("\n")