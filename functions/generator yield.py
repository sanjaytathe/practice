# x=(x+x for x in range(10))
# print(next(x))
# print(next(x))

def abc(x):
    a=1
    while a<=x:
        yield a
        a=a+1
values=abc(10)
print(next(values))
print(next(values))