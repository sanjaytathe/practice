#  Python program to count Even and Odd numbers in a List
x=[1,2,3,4,5,6,7,8,9]
even=0
odd=0
for i in x:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print("even :",even)
print("odd :",odd)