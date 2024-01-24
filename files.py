# f1=open("data.txt")
# # output = f1.read()
# # output= f1.readline()
# output= f1.readlines()
# print(f1)
# print(output)
#f1.close() # if not closed memory leakage hunxa(memory khanxa)

# f1=open("data.txt", mode="w") #mode w will over write the text in data.txt file
# f1.write("Text is overwritten")
# f1= open("data.txt") #need to write again
# output= f1.read()
# print(output)
#f1.close()

# f1=open("data.txt", mode="a") #mode a will append the text on data.txt file 
# f1.write("\nText is appended")
# f1= open("data.txt")
# output= f1.read()
# print(output)
#f1.close()

# f1=open("data.txt", mode="a") #mode a will append the text on data.txt file 
# f1.write("\nText is appended")
# f1.writelines(["Added","open"]) #multipe lines pass garna chai list banayara writelies garnu paryo
# f1.close()

# with open ('data.txt') as f: #with will automatically close the file
#     output =f.read()
#     print(output)

# print(f.closed)

name= input("Enter the name: ")
with open("name.txt","a") as f:
    f.write(f"\n{name}")
try:
    with open("name2.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("please create the file first")