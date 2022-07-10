# Python program to print even length words in a string
x=" my name is sanjay tathe sahil"
y=x.split(" ")
for i in y:
    if len(i)%2==0:
       print(i)