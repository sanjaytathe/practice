# . Python program to find second largest number in a list
x=[]

n=int(input("how many no you want to add :- "))
for i in range(n):
    v=int(input("enter the value :- "))
    x.append(v)
print(x)
x.sort()
sec_max=x[-2]
print("sec_max no is :",sec_max)