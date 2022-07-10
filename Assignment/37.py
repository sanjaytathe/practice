# . Python | Program to print duplicates from a list of integers

x=[1,2,5,3,2,4,8,9,5,6,2,1,7,1]
# y=[]
z=[]
for i in x:
    if x.count(i)>1:
        # y.append(i)
        if i not in z:
            z.append(i)
print(z)
