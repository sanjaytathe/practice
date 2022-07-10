# def san(fun):
#     def inner():
#         print(" sanjay")
#         print(" sanjay")
#         print(" sanjay")
#         fun()
#         print("tathe")
#     return inner
# def dec():
#     print(" my name is sanjay ")
# z=san(dec)
# z()

# def decor1(num):
#     def inner():
#         b=num()
#         mul=b*3
#         return mul
#     return inner
# def decor(num):
#     def inner():
#         a=num()
#         add=a+5
#         return add
#     return inner
# @decor
# @decor1
# def num():
#     return 10
# #num=decor1(num)
# print(num())

#
#
#
# # def decor(fun):
# #     def inner():
# #         d=fun()
# #         x=d['uday']=99
# #         return d
# #     return inner
# #
# #
# # def result():
# #     d={"sanjay":70,
# #        "rahul":91,
# #        "prathmesh":85}
# #     return d
# # c=decor(result)
# # print(c())
#
#
#
# def decor(num):
#     def inner(x,y):
#         c=num(x,y)
#         c=c+10
#
#         print("sum of two no is ",c)
#     return inner
# @decor
# def sum(x,y):
#     c=x+y
#     return c
# x=int(input("enter the value"))
# y=int(input("enter the value"))
# sum(x,y)
#
#
#
#
def bal(fun):
    def inner():
        tb=fun()
        t=tb-withdrawl*0.10
        #print("total available balance is")
        if withdrawl>amount:
            print("your balance is low")
        else:
            print("total available balance is")
            return t
    return inner
@bal
def bank():
    balance=amount-withdrawl
    return balance


amount=int(input("enter the amount"))
withdrawl=int(input("enter the withdrwal"))
print(bank())

#
#
#
#
#
#
#
#
#
#
#
#
# def abc(num):
#     def inner():
#         x=num()
#         return x*3
#     return inner
# def bcd(gun):
#     def outer():
#      y=gun()
#      return y+3
#     return outer
#
# @bcd
# @abc
# def sum():
#     return 10
# print(sum())