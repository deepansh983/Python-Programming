'''
Write a Python program to create a Taxi Fare Calculator that takes into account the distance traveled and the time of day. The fare calculation rules are as follows:

The base fare is ₹50 and it covers the first 5 km.
For distances between 5 km and 20 km, the fare is ₹10 per km.
For distances beyond 20 km, the fare is ₹8 per km.
If the time of day is "night", a 25% surcharge is added to the total fare.
For example, if the distance traveled is 23.5 km and the time of day is "night", the fare would be calculated as follows: Base fare: ₹50 Next 15 km: ₹150 Remaining 3.5 km: ₹28 Subtotal: ₹228 Night surcharge: ₹57 Final fare: ₹285.00

Write a Python program to implement this taxi fare calculator. You can use if-elif-else statements to segment the distance and apply the surcharge at the end, outside the distance logic.

Your task is to write a Python program that reads the distance (in km) and the time of day ("day" or "night") as input, and prints the final fare ( to 2 decimals) as output.
'''

# Take distance travelled as input (in kilometers)
distance = float(input("Enter distance travelled (in km): "))

# Take time of day (day/night), convert to lowercase for consistency
time_of_day = input("Enter time of day (day/night): ").lower()

# Base fare is Rs. 50
fare = 50.0

# Step 1: Calculate fare based on distance
if distance > 5:  
    remaining = distance - 5  # First 5 km included in base fare
    if remaining <= 15:  
        # Next 15 km charged at Rs. 10 per km
        fare += remaining * 10
    else:
        # If distance > 20 km
        fare += 15 * 10               # Charge for next 15 km
        fare += (remaining - 15) * 8 # Beyond 20 km, Rs. 8 per km

# Step 2: Apply night charges (25% extra)
if time_of_day == "night":
    fare += fare * 0.25

# Step 3: Print the final fare with 2 decimal places
print(f"Final fare: {fare:.2f}")
