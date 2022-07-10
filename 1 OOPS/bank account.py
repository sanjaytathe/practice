
class bank:
    def inputdata(self):
        self.ac_no=int(input("enter the account no"))
        self.balance=int(input("enter the balance"))
    def deposit(self):
        amt=int(input("enter the amount"))
        self.balance=self.balance+amt
    def withdrawl(self):
        amt=int(input("enter the amount"))
        self.balance=self.balance-amt
    def display_balance(self):
        print("your account no",self.ac_no)
        print("your balance",self.balance)
cust=bank()
while True:
    print('-'*30)
    choice=int(input('''
           enter your choice
           1 input your data
           2 deposit
           3 withdrawl
           4. display balance
           5 exit'''))
    print('-' * 30)
    if choice==1:
        cust.inputdata()
    elif choice==2:
        cust.deposit()
    elif choice==3:
        cust.withdrawl()
    elif choice==4:
        cust.display_balance()
    elif choice==5:
        break
    else:
        break