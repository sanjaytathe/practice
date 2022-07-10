x = []
while True:
    a = int(input('''
    1 add  element
    2 pop 
    3 last element
    4 display
    5 exit      '''))
    if a == 1:
        b = input("enter the value");
        x.append(b)
        print(x)
    elif a == 2:
        if len(x) == 0:
            print("empty")
        else:
            v = x.pop()
            print(v)
            print(x)
    elif a == 3:
        if len(x) == 0:
            print("empty")
        else:
            print("last element", x[-1])
    elif a == 4:
        if len(x) == 0:
            print("empty")
        else:
            print("display all element", x)
    elif a == 5:
        break;


