#3) Write a program to find a sum of 10 odd number using while loop   1+3+5+7+9+11+13+15+17+19
# 1st method
n=1
sum=0
while n<20:
        sum+=n      #sum=sum+n
        n+=2
print("Sum of first 10 odd number is:",sum)

#2nd method
n=0
sum=0
while n<=20:
        if n%2!=0:
            sum+=n
        n+=1
print("Sum of first 10 odd number is:",sum)