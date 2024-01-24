# List_of_numbers=[1,2,3,4]
# result=map(lambda x:x**2,List_of_numbers)
# print(list(result))
a=(lambda x,y:x-y,)(11,16)
print(a)

b=(lambda x,y,z:x*y/z)(11,16,2)
print(b)

c=(lambda x,y:x+y)(11,16)
print(c)

name=("bidhan","prikang")
result=map(lambda x:x.upper,name)
print(list(result))