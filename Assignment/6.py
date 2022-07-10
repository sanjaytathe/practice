#Python Program to find largest element in an array
# from functools import reduce
# x=[]
# sum=0
# n=int(input("how many no you want to add :- "))
# for i in range(n):
#     v=int(input("enter the value :- "))
#     x.append(v)
# print(x)
# y=reduce(lambda a,b:a if a>b else b,x)
# print(y)

#
# lst=[1,2,3,4,5,6]
# largest=0
# for i in lst:
#     if i>largest:
#         largest=i
# print(largest)

# find second largest no
l=[10,20,40,5,2,10,17,7,32,30,16]
larger=0
for i in l:
    if i>larger:
        larger=i
print(larger)
large=0
for i in l:
    if i>large and i!=larger:
        large=i
print(large)
