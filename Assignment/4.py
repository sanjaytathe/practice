# python Program for Fibonacci numbers
# n=int(input("enter the no till yuu want fibonacci series :- "))
# num1=0
# num2=1
# num3=0
# while (num3<n):
#     print(num3)
#     num1=num2
#     num2=num3
#     num3=num1+num2


n=int(input("enter the no :- "))
num1=0
num2=1
num3=0
for i in range(n):
    print(num3)
    num1=num2
    num2=num3
    num3=num1+num2
