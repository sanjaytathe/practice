# 21. Python | Multiply all numbers in the list


x=[]
mul=1
n=int(input("how many no you want to add :- "))
for i in range(n):
    v=int(input("enter the value :- "))
    x.append(v)
    mul=mul*v
print(x)
print(mul)