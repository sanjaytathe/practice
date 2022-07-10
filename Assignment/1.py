# Python Program for factorial of a number with and without recursion

# n=int(input("enter the which no you want factorial :- "))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

# def facto(n):
#       n=int(input("enter the which no you want factorial :- "))
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# print(facto(4))

def facto(n):
    if n==0:
      fact=1
    else:
        fact=n*facto(n-1)
    return fact
print(facto(5))


x=lambda i:1 if i==0 else i*x(i-1)
print(x(5))