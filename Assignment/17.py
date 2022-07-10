# Python | Reversing a List Python

a=[]
size=int(input("how many no you want to add :- "))
for i in range(size):
    val=int(input("enter the value :- "))
    a.append(val)
print(a)
i=0
j=size-1
while(i<j):
    t=a[i]
    a[i]=a[j]
    a[j]=t
    i=i+1
    j=j-1
print("reverse list is :",a)