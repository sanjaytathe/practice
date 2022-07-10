def abc(x):
    if x==0:
        fact=1
    else:
        fact=x*abc(x-1)
    return fact
fact=abc(5)
print(fact)
