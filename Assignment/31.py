# . Python program to print negative numbers in a list

x=[5,6,8,-9,-5,5,-4,2,-7]
y=[]
for i in x:
    if i<0:
        y.append(i)
print(y)