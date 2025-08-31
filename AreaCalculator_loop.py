#Write a program to create area calculator using loop
print("******Area Calculator********")
while True:
    print("""
        press 1 to get the area of square
        press 2 to get the area of rectangle
        press 3 to get the area of circle
        press 4 to get the area of triangle""")

    choice =int(input("enter a number between 1-4:\n"))

    if choice==1:
        while True:
            side=float(input("Enter the length of one side:"))
            area=side**2
            print("The area of Square is ",area)
            repeat=input("Do you want try again with square:(Yes/No)")
            if repeat=="no" or repeat=="No":
                break

    elif choice==2:
        while True:
            length=float(input("Enter the length of Rectangle:"))
            breadth=float(input("Enter the breadth of Rectangle:"))
            area=length*breadth
            print("The area of rectangle is",area)
            repeat=input("Do you want try again with rectangle:(Yes/No)")
            if repeat=="no" or repeat=="No":
                break

    elif choice==3:
        while True:
            radius=float(input("Enter the radius of circle:"))
            area=3.14*radius**2
            print("The area of circle is:",area)
            repeat=input("Do you want try again with circle:(Yes/No)")
            if repeat=="no" or repeat=="No":
                break

    elif choice==4:
        while True:
            breadth=float(input("Enter the breadth of triangle:"))
            height=float(input("Enter the height of triangle:"))
            area=0.5*breadth*height            
            print("The area of triangle:",area)
            repeat=input("Do you want try again with triangle:(Yes/No)")
            if repeat=="no" or repeat=="No":
                break

    else:
        print("Invalid input")
    repeat1=input("Do you want repeat the menu again:(Yes/NO):")
    if repeat1=="no" or repeat1=="No":
        break
print("Area Calculator signing off... Square or not, we’ll be here! 😎")       