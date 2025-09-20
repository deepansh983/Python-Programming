# this for normal approach
n = input("Enter a string: ")
char_count = {}

for ch in n:   # loop over the string, not the dictionary
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

max_char = max(char_count, key=char_count.get)
print(f"The character '{max_char}' occurs most frequently.")

#----------------------------------------------------------------------------------------------------------------

# for lexicographically order
n = input("Enter a string: ")
char_count = {}

# Count occurrences
for ch in n:
    char_count[ch] = char_count.get(ch, 0) + 1

# Find max frequency
max_freq = max(char_count.values())

# Get all characters with max frequency
max_chars = [ch for ch in char_count if char_count[ch] == max_freq]

# Pick lexicographically smallest character
max_char = min(max_chars)

print(f"The character '{max_char}' occurs {max_freq} times (highest).")
