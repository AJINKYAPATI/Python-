#loop

def fact(n):
    power=1
    for i in range(1,n+1):
        power*=i
    return power
print(fact(5))

#Recursion

def fact1(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact1(n-1)
print(fact1(5))
