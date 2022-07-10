x=int(input("enter the value"))
def evenodd():
    # x=int(input("enter the value"))
    if x%2==0:
        print("even")
    else:
        print("odd")
    def prime():
        if x<=2:
            print(" not prime no")
        else:
            for i in range(2,x):
                if x%i==0:
                    print("not prime no")
                    break
                else:
                    print("prime no")
    prime()
evenodd()