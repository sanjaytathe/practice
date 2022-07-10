def abc(num):
    def inner():
        x=num()
        return x*3
    return inner
def bcd(gun):
    def outer():
     y=gun()
     return y+3
    return outer

@bcd
@abc
def sum():
    return 10
print(sum())