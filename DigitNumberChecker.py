#write a program to check if number is single digit number
num=int(input("Enter number upto 5 digit:"))

if num>=0 and num<=9:
    print("Number is 1-digit number.")
elif num>=10 and num<=99:
    print("Number is 2-digit number.")
elif num>=100 and num<=999:
    print("Number is 3-digit number.")
elif num>=1000 and num<=9999:
    print("Number is 4-digit number.")
elif num>=10000 and num<99999:
    print("Number is 5-digit number.")
else:
    print("Number is not valid.")   