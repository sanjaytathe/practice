# Python program to remove Nth occurrence of the given word

# x=[1,2,3,4,5,6,7,8,9]
# y=int(input("which no you want to delete :- "))
# x.remove(y)
# print(x)

x=[1,2,3,4,5,6,7,8,9]
y=int(input("which no you want to delete :- "))
del x[y]
print(x)