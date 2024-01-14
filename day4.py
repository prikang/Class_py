# while loop
num=55
i=1
while i<=20:
    print(f"{num} X {i} ={num*i}")
    i+=1
    # if i==10:
    #     continue
    # elif i==15:
    #     break
    # print(f"{num} X {i} ={num*i}")
else:
    print("loop terminated")
# age=30
# while age<40:
#     print(age)

"""Ask the user name and email
only if user want to give them like (y/n)
"""

user_detail=[]
permission=input("Are you willing to provide details?: ")

while(permission=="yes"):

    name=input("Enter: ")
    user_detail.append(name)
    permission=input("Do you want to give us your email: ")
else:
    print(user_detail)


    


