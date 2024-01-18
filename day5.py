# a=12
# b=0

# try:
#     print(a/b)
# except(TypeError, ZeroDivisionError):
#     print("Can not concatenate")

# print("after handling exception")

# a=12
# b=12

# try:
#     print(a/b*c)
# except(TypeError, ZeroDivisionError,NameError):
#     print("Can not concatenate")

# print("after handling exception")

# a=12
# b=12

# try:
#    c=a/b
# except(TypeError, ZeroDivisionError,NameError):
#     print("Can not concatenate")
# else:                     #only execute if there is no exception
#     print(c)
# finally:                   #execute anyway
#     print("Finallyu execute")

# print("after handling exception")
 
# Custom invalid exceptuon
# a=12
# b=12
# class InvalidInputException(Exception):
#     pass
# try:
#    c=a/b
#    raise InvalidInputException("Input is not valid ")
# except(TypeError, ZeroDivisionError,NameError, InvalidInputException ) as e:
#     print(str(e))
#     print("Can not concatenate")
# else:                     #only execute if there is no exception
#     print(c)
# finally:                   #execute anyway
#     print("Finallyu execute")

# print("after handling exception")


a=[1,2,3]

try:
   print(a[3])
except(IndexError):
   print("Index out of range") 
else:
   print(a)
finally:
   print("finally")
print("After handling error")


