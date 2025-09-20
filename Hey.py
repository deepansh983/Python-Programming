'''
Input Format
Input consists of one line

The input consists of one line containing a single string s as specified, of length at least 3 and at most 1000.

Output Format
Output the required string with twice as many e's

Example 1
Input

hey
Output

heey
Explanation

Doubling the number of e's.

Example 2
Input

heeeeey
Output

heeeeeeeeeey
Explanation

Doubling the number of e's
'''

n = input()   # read input string
s = ''        # new string to build

for i in n:
    if i == 'e':
        s += 'e'*2   # duplicate 'e'
    else:
        s += i       # keep other characters unchanged

print(s)          # print final result
