# python program to print all Prime numbers in an Interval



# n=int(input(" enter the no :- "))
# if n<2:
#     print("not a prime no")
# else:
#     for i in range(2,n):
#         if n%i==0:
#             print("not prime")
#             break
#     else:
#           print("number is prime")



start=int(input("start of the interval :- "))
end=int(input("end of the interval :- "))
for num in range(start,end):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)










