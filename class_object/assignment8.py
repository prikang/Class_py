"""
Car Class:
Create a Car class with attributes such as make, model, and year.
Implement a method in the class to display the car details.
"""
class Car: 
    def __init__(self,make,model,year):
        self.make= make
        self.model= model
        self.year =year
    def display(self):
        return self.make, self.model, self.year
obj=Car("suzuki","Abc",2024)
result= obj.display()
print(result)

"""
Bank Account Class:
Design a BankAccount class with attributes like account number, account holder name, and balance.
Include methods to deposit and withdraw money, and display the account details.
"""
class BankAccount: 
    def __init__(self,account_number,account_holder_name,balance):
        self.account_number= account_number
        self.account_holder_name=account_holder_name
        self.balance=balance
    def display(self):
        return self.account_number,self.account_holder_name, self.balance

    def deposit(self,amount):
            self.balance=self.balance + amount
            print(f"{amount}is added ")
       

    def withdrawn(self,amount):
        self.balance= self.balance - amount
        print(f"{amount} is withdrawn")

    
    


