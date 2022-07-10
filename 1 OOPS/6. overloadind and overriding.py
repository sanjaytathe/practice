# #overloading


# class myclass:
#     def sum(self,a,b,c):
#         s=a+b+c
#         return s
#     def sum(self, a, b):
#         s = a + b
#         return s
# obj=myclass()
# # print(obj.sum(10,20,30))
# print(obj.sum(10,22))
# print(obj.sum(10,20,30))



# class myclass:
#     def sum(self,a):
#         print(" 1st sum method")
#     def sum(self):
#         print(" 2nd sum method")
# obj=myclass()
# obj.sum()
# obj.sum(10)
#
#
# class area:
#     def f_area(self,a=None,b=None):
#        if a!=None and b!=None:
#            print("area fo rect :",a*b)
#        elif a!=None:
#            print("area of squre :",a*a)
#        else:
#            print("nothing to find")
#
# obj=area()
# obj.f_area()
# obj.f_area(10)
# obj.f_area(10,20)


# ###overriding
# class add:
#     def result(self,a,b):
#         print(a+b)
# class mul(add):
#     def result(self,a,b):
#         print(a*b)
# m=mul()
# m.result(10,20)
# #
# a=add()
# a.result(10,20)
#
class add:
    def result(self,a,b):
        print(a+b)
class mul(add):
    def result(self,a,b):
        super().result(2,3)
        print(a*b)
m=mul()
m.result(10,20)
















