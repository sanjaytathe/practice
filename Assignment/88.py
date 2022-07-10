
s="a2d9t4"
k=""
for i in s:
    if i.isalpha():
        var=i
    else:
        num=int(i)
        k=k+(var*num)
print(k)
