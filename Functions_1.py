# with out return type without para
def greet():
    print("Hello")
    greet()

def get_number(n):
    print(n*n)
    get_number(10)

def add(a,b):
    return a+b
    print(add(10,20))
    ans=add(10,20)
    print(ans)
        
# with return type without para
def mul():
    return 2*2
print(mul(+2))
op=mul()
print(op+10*2)

##with return type with para by taking user ip
num=int(input("enter a number: "))
def cube(num):
    return num*num*num
print(cube(num))
