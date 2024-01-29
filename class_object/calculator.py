class Calculator:
    def __init__(self,num1, num2):
        self.num1=num1
        self.num2=num2
    
    def add(self):
        return self.num1 + self.num2

    
    def multiplication(self):
        return self.num1 * self.num2
    
number1= int(input("enter the number1: "))
number2= int(input("enter the number2: "))

obj1= Calculator(num1=number1, num2=number2)
result1= obj1.add()
result2= obj1.multiplication()
print(result1)
print(result2)




