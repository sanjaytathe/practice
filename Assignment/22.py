# Python program to find smallest number in a list


# x=[]
#
# n=int(input("how many no you want to add :- "))
# for i in range(n):
#     v=int(input("enter the value :- "))
#     x.append(v)
# print(x)
# min=min(x)
# print("min no is :",min)

from functools import reduce
x=[15,3,6,8,4]
y=reduce(lambda x,y:x if x<y else y,x)
print(y)