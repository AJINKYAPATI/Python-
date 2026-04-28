n=4
i=n
while i>=1:
    j=1
     while j<=i:
        if i%2==0:
            print("1",end="")
        else:
            print("0",end="")
        j+=1
    print("")
    i-=1
