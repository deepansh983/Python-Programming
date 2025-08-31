num=int(input("Enter number:"))
original=num
reverse=0
while num>0:
    digit=num%10                   #get last digit
    reverse=reverse*10+digit       #append the digit to reverse
    num=num//10                    #remove the last digit
if (original==reverse):
    print(original,"is a palindrome number")
else:
    print(original,"is not a palindrome")        