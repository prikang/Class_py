import csv

with open("files/stock_data.csv", "r") as mero_file:
    reader = csv.DictReader(mero_file)
    companies=[]
    for row in reader:
        if float(row["Percent Change"].split("%"[0]))>0:
            companies.append(row["Symbol"])

with open("files/names.csv","a") as mero_file:
    filenames=["name","email"]
    reader=csv.Dictwriter(mero_file,filenames=filenames)
      #reader.writerow({"name":"hari","email":"hari@2"})


class People:
    def __init__(self, age): #__repr__ __str__. magic dember menthod
        self.age = age

    def under_16(self):
        if self.age<16:
            return True
        return False

obj1 = People(age=15)
result = obj1.under_16()

print(result)

obj2= People(age=32)
obj2.under_16()