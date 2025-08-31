# Write a program to check the number is prime or not
num=int(input("Enter number to check for prime number:"))
#prime number are greater than 1 and 1 is neither prime nor composite
if num<=1:
    print(num,"is not a prime number")
else:    
    for i in range(2,num):      
        if num%i==0:
            print(num,"is not a prime number")
            break
    else:
        print(num," is a prime number")
         