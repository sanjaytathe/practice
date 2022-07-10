name=[]
n=int(input("enter the number"))
for x in range(n):
   a=int(input("enter the name"))
   name.append(a)
s=set(name)

name=list(s)
print(name)