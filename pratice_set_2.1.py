# #Write a program to check if a number is a single digit number,
#2-digit number and so on ... up to 5 digits.
num = int(input("enter a number here: "))
if num >=0 and num<=9:
    print("number is single digit number")

elif num>=10 and num<=99:
    print("number is 2-digit number")

elif num>=100 and num<=999:
    print("number is 3-digit number")

elif num>=1000 and num<=9999:
    print("number is 4-digit number")

elif num>=10000 and num<=99999:
    print("number is 5-digit number")

else:
    print("number is out of range (not 1-5 digits)")
