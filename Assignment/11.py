# . Python program to interchange first and last elements in a list


x=[]

n=int(input("how many no you want to add :- "))
for i in range(n):
    v=int(input("enter the value :- "))
    x.append(v)
print(x)
c=x[0]
x[0]=x[-1]
x[-1]=c
print(x)
