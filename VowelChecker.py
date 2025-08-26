#write a program to check whether passed letter is vowel or not
letter=str(input("Enter the Letter:"))

if letter in "aeiou" or letter in "AEIOU":             #we check the string with the help of check string using keyword in
 print("Letter is vowel")
else:
 print("letter is constant")