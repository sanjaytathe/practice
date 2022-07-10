# 1) Write a program to check whether the given file exist or not. If it is available then print its
# content?

# import os
# print(os.path.isfile('sss.txt'))
#-----------------------------------------------------------------------------------------------------------------------

# 2) VWrite a function in Python to count and display the total number of words in a text file.
# def countd():
#  s=open("sss.txt",'r')
#  count=0
#  t=s.read()
#
#  for i in t:
#   count=count+1
#  s.close()
#  print(count)
# countd()
#-----------------------------------------------------------------------------------------------------------------------
# 4. Write a function in Python to count uppercase character in a text file

# def upper1():
#   s=open("sss.txt",'r')
#   count=0
#   t=s.read()
#   for i in t:
#     if i.isupper():
#       count=count+1
#
#
#   s.close()
#   print(count)
# upper1()
#------------------------------------------------------------------------------------------------------------------------

# def countd():
#   f=open("sss.txt",'r')
#   V=C=U=L=0
#   data=f.read()
#   for i in data:
#     if i.isalpha():
#       if i.isupper():
#         U=U+1
#       if i.islower():
#           L=L+1
#       if i in 'aeiouAEIOU':
#         V=V+1
#       else:
#         C=C+1
#
#   print(U)
#   print(L)
#   print(V)
#   print(C)
# countd()
#-----------------------------------------------------------------------------------------------------------------------

# Write a function in Python to count words in a text file those are ending with alphabet "e"

# s=open("sss.txt",'r')
# t=s.read()
# y=t.split()
# # print(y)
# for i in y:
#     if i[-1]=='e':
#         print(i)

#------------------------------------------------------------------------------------------------------------------------

# Write a function in Python to read lines from a text file. Your function should find and display
# the occurrence of the word "the"

# def countd():
#     f=open("sss.txt",'r')
#     t=f.read()
#     d=t.split()
#
#     count=0
#     for i in d:
#         if i=="the":
#             count=count+1
#     print(count)
#     f.close()
# countd()

#------------------------------------------------------------------------------------------------------------------------