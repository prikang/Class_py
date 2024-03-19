class Bank:
    def get_name(self):
        return "ABC Bank"
    
    def get_interest(self):
        return 10

class Customer(Bank):
    def __init__(self, name,phone_number)->None: 
        self.name= name
        self.phone_number=phone_number

class CustomerAccoutDetail(Customer, Bank):
    BALANCE=0
    def __init__(self, name,phone_number)
        self.customer = Customer(name= name, phone_number=phone_number)

    def get_balance(self):
        return self.BALANCE


    def get_customer_detail(self):
        return{
            "name": self.customer.name,
            "phone number":self.customer.phone_number
        }

account_details=CustomerAccoutDetail()