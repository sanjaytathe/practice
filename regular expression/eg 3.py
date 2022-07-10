# text='''this is me
# and my name
# is abhishek roo no-46879879
#
# this is no-2,no-12
# no-34566 me abhinav moc no-8087849140
# '''
#
# import re
# s=re.findall('no-\d{3}',text)
# print(s)



# import re
# # s=re.findall(r'no-[0-9]{1,3}',text)
# # print(s)
#
# s=re.findall(r'no-\d{1,3}',text)
# print(s)


# import re
# text="abhishek abhinav abhinandan ABHinav abhay sanjay pavan sahil"
# s=re.findall(r'abhi[a-z]*',text,flags=re.I)
# print(s)


# import re
# str='XCG-456 is the battary one,FHD123 and serial no ABC 789'
# s=re.findall(r'[A-Z]+[-| ]*\d*',str)
# print(s)



import re
text="belt melt bellet mallet abhishek"
s=re.findall(r'[a-z]*lt',text)
print(s)