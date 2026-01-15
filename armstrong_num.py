num=int(input("enter a number :"))
temp=num
sum=0
while num>0:
    digit=num%10
    sum=sum+digit**3
    num=num//10
if sum==temp:
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")
