# 1) Write a program to find a sum of all even numbers upto 50.   0+2+4+6+8+10+......+50

sum=0
#Taking for loop from 0 to 50
for i in range(0,51):
    #check for the number is even or not
    if i%2==0:
        sum+=i     #sum=sum+i    0+2,2+4,6+4,10+6,16+12.........602+48
print("Sum of all even number upto 50 is:",sum)        


