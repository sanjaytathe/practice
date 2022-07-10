# Python Program for array rotation
x=[]
sum=0
n=int(input("how many no you want to add :- "))
for i in range(n):
    v=int(input("enter the value :- "))
    x.append(v)
print(x)
n=int(input("do you want to rotate by what no :- "))
for i in range(n):
    popEle=x.pop(0)
    x.append(popEle)
print(x)