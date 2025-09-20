'''
Good Strings
You are given a set 'S' of distinct characters. You are also given an array 'A' of 'N' strings.

A String in array 'A' is called good if all the characters of the string is present in the set 'S'.

You have to find how many strings in the array 'A' are good.

Input Format
The first line contains the number of test cases.

For each test case: The first line contains a string denoting the characters of the set 'S'.

The next line contains 'N', the number of strings in 'A'.

The next 'N' lines contains a string each, which are the elements of the array 'A'.

Output Format
For each test case print the count of good strings in a new line.

Example 1
Input:

1
abc
4
ab
abd
cacb
cabef
'''

t = int(input())   # number of test cases

for _ in range(t):
    allowed = set(input().strip())   # set S (allowed characters)
    
    n = int(input())   # number of strings in array A
    
    count = 0
    for _ in range(n):
        word = set(input().strip())
        if word.issubset(allowed):   # check if word is "good"
            count += 1
    
    print(count)
