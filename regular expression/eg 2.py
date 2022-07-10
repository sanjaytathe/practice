# import re
# email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
# user_email=input("enter your emil")
# if re.search(email_condition,user_email):
#     print("right email")
# else:
#     print("wrong email")


# text='''this is me
# and my name
# is abhishek roo no-46879879
#
# this is no-2,no-12
# no-34566 me abhinav moc no-8087849140
#  '''
#
# import re
# s=re.findall('no-\d{3}',text)
# print(s)


#
# import re
# s=re.findall('no-[0-9]{1,5}',text)
# print(s)

# s=re.findall(r'no-\d{1,3}',text)
# print(s)

#
# import re
# text="abhishek abhinav abhinandan ABHinav abhay sanjay pavan sahil"
# s=re.findall('abhi[a-z]*',text,flags=re.I)
# print(s)
#

# import re
# str='XCG-456 is the battary one,FHD123 and serial no ABC 789'
# s=re.findall(r'[A-Z]+[-| ]*\d*',str)
# print(s)


#
# import re
# text="belt melt bellet mallet abhishek"
# s=re.findall(r'[a-z]*lt',text)
# print(s)

#
# import re
# c_score='''Sachin scores 76 and Dravid scores 89 and Rohit scores 267'''
# # print(c_score)
# name=re.findall(r'[A-Z][a-z]*',c_score)
# print(name)
# score=re.findall('\d[0-9]*',c_score)
# print(score)
# score=re.findall('\d{2}',c_score)
# print(score)

#
# d={}
# i=0
# for x in name:
#     d[x]=score[i]
#     i=i+1
# print(d)

# c=dict(zip(name,score))
#
# print(c)
#


# import re
# str="my name is sanjay and sanjay is good boy"
# if re.search("sanjay",str):
#     print("item found")
#     match=re.findall("sanjay",str)
#     for i in match:
#          print(i)
# for i in re.finditer("sanjay",str):
#     index=i.span()
#     print(index)

#
# import re
# str="Rat Cat Mat Sat"
# data=re.findall('[PMR]at',str)
# print(data)

#
# import re
# str="Rat Cat Mat Sat"
# data=re.findall('[^R]at',str)
# print(data)



import re
str='''how are you
i am fine
thank you'''
reg=re.compile('\n')
str=reg.sub('-',str)
print(str)


import re
x="^[a-z]+[0-9]+[\._]?[@][a-z]+[.][a-z]{2,3}"
y=input("enter the password :- ")
if re.search(x,y):
    print("right password")
else:
    print("wrong password")

# import re
# x='16845dshfvjerbjhtvb6546'
# print(len(re.findall('\D',x)))


# import re
# x="melt geklt prltd bullet"
# print(re.findall('[a-z]*lt',x))








# import re
# s='1234567789'
# print("no of digit",len(re.findall('[0-9]',s)))




# import re
# s='dgsdg1234567789'
# print("no of digit",len(re.findall('\D',s)))


import re

str1 = "/*Jon is @developer & musician"
t=re.sub("[^a-zA-z\s]+","",str1)
print(t)