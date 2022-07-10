# Python Program to find sum of list
# x=[]
# sum=0
# n=int(input("how many no you want to add :- "))
# for i in range(n):
#     v=int(input("enter the value :- "))
#     x.append(v)
#     sum=sum+v
# print(x)
# print(sum)


x=[]

n=int(input("how many no you want to add :- "))
for i in range(n):
    v=int(input("enter the value :- "))
    x.append(v)

print(x)
print(sum(x))