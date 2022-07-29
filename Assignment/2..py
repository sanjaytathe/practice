# # Python Program to check Armstrong Number
#
# n=int(input("enter number to check for armstrong :- "))
# orig=n
# sum=0
# while(n>0):
#     sum=sum+(n%10)*(n%10)*(n%10)
#     n=n//10
# if orig==sum:
#     print("Number is armstrong")
# else:
#     print("Number is not armstrong")


lower = 100
upper = 2000

for num in range(lower, upper + 1):

    # order of number
    order = len(str(num))

    # initialize sum
    sum = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        print(num)

