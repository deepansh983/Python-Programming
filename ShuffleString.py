'''
Shuffle String
Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Print the shuffled string.

Input Format
Input consists of two lines.

First line contains an integer n.

Second line contains the string.

Last line contains the indices separated by space.

Output Format
Print the shuffled string.

Example 1
Input

8
acciojob
4 5 6 7 0 2 1 3
Output

oojbacci
Explanation

As the problem states "acciojob" becomes "oojbacci" after shuffling.

Example 2
Input

3
abc
0 1 2
Output

abc
Explanation

No shuffling is done here.
'''

n = int(input())              # length of string
s = input()                   # the string
indices = list(map(int, input().split()))  # indices list

# create empty result list of the same size
result = [""] * len(s)

# place each character in its new position
for i in range(len(s)):
    result[indices[i]] = s[i]

# join into final string
s_str = "".join(result)

print(s_str)
