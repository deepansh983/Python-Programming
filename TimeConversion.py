# Take input time in 12-hour format with AM/PM (e.g., "07:05:45PM")
s = input()

# Extract hours, minutes, seconds, and period from the input string
hours = s[0:2]      # First two characters → hour
hour = int(hours)   # Convert hour to integer for calculation
minute = s[3:5]     # Characters at position 3–4 → minutes
second = s[6:8]     # Characters at position 6–7 → seconds
period = s[8:10]    # Last two characters → AM or PM

# Convert 12-hour format to 24-hour format
if period == 'AM':
    if hour == 12:
        hour = 0    # Special case: 12 AM → 00 hours (midnight)
    else:
        hour = hour # For AM hours other than 12, keep the same value
elif period == 'PM':
    if hour != 12:
        hour += 12  # For PM hours (except 12 PM), add 12 to convert to 24-hour format

# Format hour with two digits (e.g., "00", "01", ..., "23")
hour_str = f"{hour:02d}"

# Build the final 24-hour format time string
result = hour_str + ':' + minute + ':' + second

# Print the result
print(result)



