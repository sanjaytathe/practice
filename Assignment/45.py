# ython | Count the Number of matching characters in a pair of string

x=input("enter the string")
count=0
y=x.split(" ")
for i in y:
    if i=="the":
        count=count+1
print(count)