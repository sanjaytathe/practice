# Python program to count positive and negative numbers in a list

x=[1,2,-3,4,-5,6,7,8,-9]
pos=0
neg=0
for i in x:
    if i>=0:
        pos=pos+1
    else:
        neg=neg+1
print("positive no :",pos)
print("negative no :",neg)