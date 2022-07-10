# n program to find Cumulative sum of a list Break a list into chunks of size N in
l=[]
for i in range(1,6):
    n=int(input("enter the value :- "))
    l.append(n)
n = 4
x = [l[i:i + n] for i in range(0, len(l), n)]
print(x)