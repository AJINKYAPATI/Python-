num=int(input("enter the number: "))
sum=0
temp=num

while num>0:
    rem=num%10
    sum=(sum*10)+rem
    num//=10
    print("The reversed number is:",sum)

    if temp==sum:
        print("It is a palindrome number")
    else:
        print("It is not a palindrome number")
