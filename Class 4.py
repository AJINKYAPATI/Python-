class student:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city

name=input("enter name\n")
age=int(input("enter age\n"))
city=input("enter city\n")

s1=student(name,age,city)
print(s1.name,s1.age,s1.city)
