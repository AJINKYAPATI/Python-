# # write a program to create a building system at supermarket.
while True:
    name = input("enter customer name:  ")
    total = 0

    while True:
        print("enter the amount and quantity")
        amount = float(input("enter amount: "))
        quantity = float(input("enter quantity: "))
        total += amount * quantity
        repeat = input("Do you want to add more itema ? ")
        if repeat == "no" or repeat == "no":
            break

        print("-"*40)
        print("Name: ", name)
        print("amount to be paid: ", total)
        print("-"*40)
        print("************* Happy Shopping************")

        repeat1 = input("DO you want to go to next customer ? (yes/No): ")
        if repeat1 == "no" or repeat == "no":
            break
