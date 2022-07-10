#  Write a program to find number of occurences of each character of each letter present in the
# given string?
# x=input("enter the string :- ")
# l=[]
# for i in x:
#
#     if i not in l:
#         l.append(i)
#
#         print(i,"occured",x.count(i),"times")

# without count method
# d={}
# for i in x:
#     d[i]=d.get(i,0)+1
# print(d)


x="sanjay"
d={}
for i in x:
    v=(x.count(i))
    d[i]=v
print(d)