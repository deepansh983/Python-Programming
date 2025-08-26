# Write a program to create area calculator
print("******Area Calculator********")
print("""
      press 1 to get the area of square
      press 2 to get the area of rectangle
      press 3 to get the area of circle
      press 4 to get the area of triangle""")

choice =int(input("enter a number between 1-4:\n"))

if choice==1:
    side=float(input("Enter the length of one side:"))
    area=side**2
    print("The area of Square is ",area)

elif choice==2:
    length=float(input("Enter the length of Rectangle:"))
    breadth=float(input("Enter the breadth of Rectangle:"))
    area=length*breadth
    print("The area of rectangle is",area)

elif choice==3:
    radius=float(input("Enter the radius of circle:"))
    area=3.14*radius**2
    print("The area of circle is:",area)

elif choice==4:
    breadth=float(input("Enter the breadth of triangle:"))
    height=float(input("Enter the height of triangle:"))
    area=0.5*breadth*height            
    print("The area of triangle:",area)

else:
    print("Invalid input")