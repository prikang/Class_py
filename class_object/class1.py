# class vechile:
#     def __init__(self):  #int = constructor
#      print("Called")

# truck= vechile()

class People:
    def __init__(self, age): #__repr__ __str__. magic dember menthod
        self.age = age

    def under_16(self):
        # self.hello()
        if self.age<16:
            return True
        return False

obj1 = People(age=15)
result = obj1.under_16()

print(result)

obj2= People(age=32)
obj2.under_16()