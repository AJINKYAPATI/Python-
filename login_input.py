username=input("enter username: ")
password=input("enter password: ")
if username == "admin" and password == "1234":
    print("login successful")
elif username == "admin" and password != "1234":
        print("invalid password")
elif username != "admin" and password == "1234":
        print("invalid username")   
else:
    print("login fail")
