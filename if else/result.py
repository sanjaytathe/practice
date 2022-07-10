n=int(input(" enter the no :- "))
if n<2:
    print("not a prime no")
else:
    for i in range(2,n):
        if n%i==0:
            print("not prime")
            break
    else:
          print("number is prime")
