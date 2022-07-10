# sum=lambda a,b:a+b
# print(sum(10,2))

# fact=lambda i:1 if i==0 else i*fact(i-1)
# print(fact(5))

# num=[2,4,6,8]
#
# add=map(lambda n:n*n,num)
# print(list(add))

# list1=[2,4,6,8]
# list2=[1,3,5,7]
# add=map(lambda x,y:x+y ,list1,list2)
# print(list(add))


try:
    age=int(input("enter your age : "))
    if age<0:
        raise ValueError
    print("your age is :",age)
except ValueError:
    print("enter valid age")
print("rest of the code")