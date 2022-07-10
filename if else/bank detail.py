bal=0
while True:
    print('-' * 30)
    choice = int(input('''
               enter your choice
               1 input your data
               2 deposit
               3 withdrawl
               4. display balance
               5 exit'''))
    print('-' * 30)
    if choice==1:
        ac_no = input("enter your name")
        bal = int(input("enter your balance"))
    elif choice==2:
        amt=int(input("enter the deposit amount"))
        bal=bal+amt
    elif choice==3:
        amt=int(input("enter the withdrawl amount"))
        bal=bal-amt
    elif choice==4:
        print(ac_no)
        print(bal)
    elif choice==5:
        break