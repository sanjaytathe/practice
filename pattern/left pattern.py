n = int(input("enter the number rows"))
for i in range(n+1):
    for j in range(n - i):
        print(" ", end=" ")
    for x in range(i):
        print("*", end=" ")
    print()

