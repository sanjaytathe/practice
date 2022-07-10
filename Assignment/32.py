# . Python program to print all positive numbers in a range

start=int(input("enter start no :- "))
end=int(input("enter start no :- "))
for i in range(start,end+1):
    if i>=0:
        print(i)