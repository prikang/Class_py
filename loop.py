fruits = ["Mango" ,"Berry" ,"Orange"]

# for fruit in fruits:
#     print(fruit)

# [print(fruit) for fruit in fruits if fruit=="Mango"] #list comperhenshive 

# for fruit in fruits:
#     if fruit=="Berry":
#         print("Will break the program")
#         break
#     print(fruit)

# for fruit in fruits:
#     if fruit=="Berry":
#         continue
#         print("Will execute the program?")
#     print(fruit)

# for fruit in fruits:
#     if fruit=="Berry":
#         pass
#         print("Will execute the program?")
#     print(fruit)   

# for i in range(1,10,2):
#     print(i)
    

# for i in range(10,21):
#     print(f"startingiteration {i}")
#     if i==15:
#         continue 
#     elif i==16:
#         pass

#     elif i==17:
#         break   
#     else:
#         print(i)

#     print(f"ending iteration {i}")


datas=[1,2,500,900,666,"999",88,"abcd",55,"5555"]
for data in datas:
    if isinstance(data,int):
        print(data)

    elif data.isdigit():
        print("Digit detected")
    else:
        print(f"oops!{data} is not valid digit")
        break

# assignment
    