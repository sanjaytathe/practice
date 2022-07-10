# def evenodd(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# list1=[2,3,4,5,6,7,8]
# result=list(filter(evenodd,list1))
# print(result)
#
# for i in result:
#     print(i)
#

# list1=[1,2,3,4,5,6,7]
# result=lambda x:x if x>2 else None
# print(result(list1))
#
val=[1,2,3,4,5,6,7,8,9]
d=list(filter(lambda a:a%2==0,val))
print(d)
# for x in d:
#     print(x)
#
# list1=[1,2,3,4,5,6,7]
# result=list(filter(lambda x:True if x%2==0 else False,list1))
# print(result)


#x=[1,2,3,4,5,6,7,8,9]
# evenodd=list(filter(lambda a:a%2==0,x))
# squre=list(map(lambda a:a*a,evenodd))
# print(evenodd)
# print(squre)

#
# x=[1,2,3,4,5,6,7,8,9,14]
# def d(x):
#  if x%2==0:
#     return True
#  else:
#      return False
# def sqrt(x):
#      return x*x
# e=list(filter(d,x))
# print(e)
# s=list(map(sqrt,e))
# print(s)