'''
Question 3: Second-Largest Finder

You are working as a data analyst in a financial institution, and you need to develop a program to identify the second-largest value among four distinct integers. This program will be used to analyze the performance of different investment portfolios. The program should read four distinct integers as input and determine the second-largest value using only if/elif/else statements (without using loops, sorted(), or max() functions).

For example, if the input is 12 7 19 5, the output should be 12.

Write a Python program to achieve this task.
'''

# Take 4 distinct integers as input in one line, separated by space
a, b, c, d = map(int, input("Enter four distinct integers: ").split())

# Step 1: Find the largest number among a, b, c, d
if a > b and a > c and a > d:
    largest = a
elif b > a and b > c and b > d:
    largest = b
elif c > a and c > b and c > d:
    largest = c
else:
    largest = d

# Step 2: Depending on which one is largest, find the second largest
if largest == a:
    # If 'a' is the largest, then second largest is the maximum of b, c, d
    if b > c and b > d:
        second = b
    elif c > b and c > d:
        second = c
    else:
        second = d
elif largest == b:
    # If 'b' is the largest, then second largest is the maximum of a, c, d
    if a > c and a > d:
        second = a
    elif c > a and c > d:
        second = c
    else:
        second = d
elif largest == c:
    # If 'c' is the largest, then second largest is the maximum of a, b, d
    if a > b and a > d:
        second = a
    elif b > a and b > d:
        second = b
    else:
        second = d
else:
    # If 'd' is the largest, then second largest is the maximum of a, b, c
    if a > b and a > c:
        second = a
    elif b > a and b > c:
        second = b
    else:
        second = c

# Step 3: Print the second largest number
print("Second largest:", second)
