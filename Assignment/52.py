#  Python program to find uncommon words from two Strings
# def function(a,b):
#     list_a=a.split()
#     list_b=b.split()
#     uc=' '
#     for i in list_a:
#         if i not in list_b:
#             uc=uc+" "+i
#     for j in list_b:
#         if j not in list_a:
#             uc=uc+" "+j
#     return uc
#
# a="apple banna ,mango"
# b="banna,fruti,mango,"
# print(function(a,b))


a="apple ,banna ,mango"
b="banna,fruti,mango,"
x=a.split(",")
y=b.split(",")
v=set(x).difference(set(y))
print(v)