#  Python program to find the sum of all items in a dictionary

x={'x':100,'y':200,'z':500}
sum=0
for i in x.values():
    sum=sum+i
print(sum)