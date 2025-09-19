'''
Write a Python program that implements a Triangle Analyzer. The program should read three positive integers a, b, c (the side lengths) and checks if they can form a triangle .

Valid Triangle Conditions:

(a + b > c, a + c > b, and b + c > a).

If the triangle is not valid, print "Invalid triangle".

If the triangle is valid, classify it by sides (Equilateral, Isosceles, or Scalene) and by angles (Right-angled, Acute, or Obtuse). Finally, print both classifications on one line.

For example, if the input is 3 4 5, the output should be "Scalene Right-angled". If the input is 2 2 3, the output should be "Isosceles Acute".
'''


# Take input for three sides of the triangle
a, b, c = map(int, input("Enter three side lengths: ").split())

# Step 1: Check triangle validity using Triangle Inequality Theorem
# For a valid triangle, sum of any two sides must be greater than the third
if not (a + b > c and a + c > b and b + c > a):
    print("Invalid triangle")
else:
    # Step 2: Classify triangle based on side lengths
    if a == b == c:
        side_type = "Equilateral"     # All sides equal
    elif a == b or b == c or a == c:
        side_type = "Isosceles"       # Any two sides equal
    else:
        side_type = "Scalene"         # All sides different

    # Step 3: Sort sides to identify the largest side (z)
    sides = sorted([a, b, c])
    x, y, z = sides  # x, y are smaller sides; z is the largest side

    # Step 4: Classify triangle based on angles using Pythagoras theorem
    if x**2 + y**2 == z**2:
        angle_type = "Right-angled"   # Pythagoras holds -> Right triangle
    elif x**2 + y**2 > z**2:
        angle_type = "Acute"          # Sum of squares of smaller sides > largest side^2
    else:
        angle_type = "Obtuse"         # Sum of squares of smaller sides < largest side^2

    # Step 5: Print the classification result
    print(side_type, angle_type)
