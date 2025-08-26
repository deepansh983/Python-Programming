# Write a program create a billing system of supermarket
while True:
    name=input("Enter customer's name:")
    total=0

    while True:
        print("Enter the amount and quantity:")
        amount=float(input("Enter amount:"))
        quantity=int(input("Enter Quantity:"))
        total+=amount*quantity

        repeat=input("Do you want add more item to cart! (Yes/No):")
        if repeat=="No" or repeat=="no":
            break
    print("-"*40)
    print("Name:",name)
    print("Amount to be paid:",total)
    print("-"*40)
    print("**************Thank you for Shopping Here**************")
    bill=input("Make a copy of bill and print:Yes/NO:")
    print("Bill printed")
    repeat1=input("Do you want to add new bill for another customer!(Yes/No):")
    if repeat1=="No" or repeat1=="no":
        break