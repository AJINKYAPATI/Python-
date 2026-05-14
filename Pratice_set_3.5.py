# # write a program to create a building system at supermarket.

while True:
    name = input("Enter customer name: ")
    total = 0

 while True:
        print("\nEnter the amount and quantity")
        amount = float(input("Enter amount: "))
        quantity = float(input("Enter quantity: "))
        
        total += amount * quantity

        repeat = input("Do you want to add more items? (yes/no): ").lower()
        if repeat == "no":
            break

# Bill printing (outside inner loop)
    print("\n" + "-" * 40)
    print("Name:", name)
    print("Amount to be paid: ₹", total)
    print("-" * 40)
    print("************* Happy Shopping *************")

    repeat1 = input("\nDo you want to go to next customer? (yes/no): ").lower()
    if repeat1 == "no":
        break
