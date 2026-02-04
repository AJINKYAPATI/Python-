s="InDia123"
u=l=d=0
for i in s:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
    elif i.isdigit():
        d+=1
print("u :",u,"l:",l,"d:",d,"length:",len(s))
