#  Python program to print all even numbers in a range
start=int(input("enter start no :- "))
end=int(input("enter end no :- "))
for i in range(start,end+1):
    if i%2==0:
        print(i)