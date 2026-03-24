

class BankAccount:
    # para con
    def__init__(self,name,bal):
        self.name=name
        self.bal=bal

    # withdraw
    def withdraw(self,amount):
        self.amount=amount
        return self.bal-amount
    
    #deposit
    def deposit(self,amount):
        self.amount=amount
        op= self.bal+amount
        print(amount,"credied & av bal is",op)

        #check bal
        def checkbal(self):
            print("av bal is ",self.bal)


U1=BankAccount("Ram",1000);
U1.deposit(2000)
print(U1.deposit(5000))
U1.checkbal()
