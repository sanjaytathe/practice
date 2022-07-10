## Python | Program to accept the strings which contains all vowels
s=input("enter the string :- ")
v="aeoiu"
t=set(s).intersection(v)
print(type(t))
if t==set(v):
    print("yes")
else:
    print("no")













































