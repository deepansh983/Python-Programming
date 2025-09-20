'''
Pangrams
A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.

Input Format
The first line inputs a string, S.

Output Format
In a new line, print "pangram" if string contains every letter of the alphabet else "not pangram".

Example 1
Input

We promptly judged antique ivory buckles for the next prize
Output

pangram
Explanation All of the letters of the alphabet are present in the string.

Example 2
Input

We promptly judged antique ivory buckles for the prize
Output

not pangram
Explanation

The string lacks an x.
'''

alphabet_set = {chr(i) for i in range(97, 123)}  # a-z

n = input("Enter a sentence: ").lower()  # convert everything to lowercase
N = set(n)  # unique characters from input

if alphabet_set.issubset(N):   # check if all a-z are present
    print("pangram")
else:
    print("not pangram")
