def decor(func):
    def inner(name):
        if name == "sunny":
            print("Hello Sunny Bad Morning")
        else:
            func(name)

    return inner


@decor
def wish(name):
    print("Hello", name, "Good Morning")


# decorfunction=decor(wish)
# decorfunction("sunny")
wish("sunny")

#
# def abc(num):
#     def inner(name):
#         #d=num(name)
#         if name=="sunny":
#             print("hello sunnt bad morning")
#         else:
#             num(name)
#     return inner
# @abc
# def wish(name):
#     print("hello",name,"good morning")
# wish("sanjay")
