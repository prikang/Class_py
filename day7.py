"""
Write a fubction that uses list comorehenshive to generate a list of squares of number from 1 to n
"""

n=int(input("Enter the number: ") )
def generate_square(number):
    return number**2

def generate_square_of_list_of_numbers(*args):   #*args: number of argumnet to accept (dherai ota argumnet aauxa vane we should keep *args)
    # print(args)
    # for arg in args:
    #     print(arg)
    #     print(generate_square(arg))
    return[generate_square (arg) for arg in args]
List_of_numbers= range(1, n+1)
# print(List_of_numbers) #print only range (1,7)
# print(*List_of_numbers) #print (1,2,3,4,5,6,7)

results=generate_square_of_list_of_numbers(*List_of_numbers)
print(results)
