# WAP (Write A Program) to find max and min in a set
a = {10, 2, 4, 2, 54, 6, 7, 41, 65, 41, 63, 48, 12, 33, 66, 77, 80}

# max() returns the largest element, min() returns the smallest element
maximum = max(a)
minimum = min(a)

print("The maximum of set a is:", maximum)
print("The minimum of set a is:", minimum)


# WAP to find common elements in three lists using sets
a = [10, 2, 3, 4, 5, 6, 8]
b = [4, 5, 7, 6, 3, 2, 1]
c = [6, 7, 1, 4, 2, 3, 6, 5]

# Convert lists to sets, then use '&' (intersection operator)
print(set(a) & set(b) & set(c))   # prints common elements


# WAP to find difference between two sets
a = {1, 2, 6, 3, 5}
b = {4, 5, 6, 8, 9}

# difference_update() removes common elements of b from a
a.difference_update(b)
print(a)   # a now contains only {1, 2, 3}


# WAP to remove an item from set if it is present in set
a = {1, 2, 6, 3, 5}

# discard() removes element if present, else does nothing (safe version of remove())
a.discard(5)
print(a)   # {1, 2, 3, 6}


# WAP to check if a set is a subset of another set
a = {1, 2, 3, 4, 5, 6, 7, 8}
b = {1, 4, 5, 6}

# issubset() checks if all elements of b exist in a
print(b.issubset(a))   # True
