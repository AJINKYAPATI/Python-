def printnum(n):
    
    if n==0:
        return
    printnum(n-1)
    print(n)
printnum(7)
