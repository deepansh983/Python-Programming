from datetime import datetime

# Take input time in 12-hour format (e.g., "07:05:45PM")
s = input()

# Parse the 12-hour format and convert to 24-hour format
result = datetime.strptime(s, "%I:%M:%S%p").strftime("%H:%M:%S")

print(result)

# ------------------------------
# Sample Inputs and Outputs:
# Input:  "12:00:00AM" → Output: "00:00:00"
# Input:  "01:23:45AM" → Output: "01:23:45"
# Input:  "12:00:00PM" → Output: "12:00:00"
# Input:  "07:05:45PM" → Output: "19:05:45"
# ------------------------------
