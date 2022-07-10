# Python | Check if a given string is binary string or not

# x=input("enter the string :- ")
# for i in x:
#     if i in "10":
#         pass
#     else:
#         print("given string is not binary")
#         break
# else:
#     print("given string is binary")


x=input("enter the string :- ")
for i in x:
    if i not in "10":
        print("given string is not binary")
        break
else:
    print("given string is binary")
