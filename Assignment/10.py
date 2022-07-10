# Python Program for Find reminder of array multiplication divided by n

x=[]
mul=1
n=int(input("how many no you want to add :- "))
for i in range(n):
    v=int(input("enter the value :- "))
    x.append(v)
    mul=mul*v
print(x)
print(mul)
n=int(input("by what no you want t divide :- "))
remainder=mul%n
print("remainder is ", remainder)


