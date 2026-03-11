def printnum(n):
    if n==0:
        return
    print(n)
    printnum(n-1)

printnum(5)
