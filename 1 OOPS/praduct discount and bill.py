class product:
    def inputdata(self):
        self.pname=input("enter product name")
        self.price=int(input("enter the product price"))
        self.qty=int(input("enter the product quantity"))
    def calculation(self):
        self.discount=(self.price*self.qty)*0.10
        self.bill=(self.price*self.qty)-self.discount
        print(self.discount)
        print(self.bill)
prod1=product()
prod2=product()
prod1.inputdata()
prod1.calculation()
prod2.inputdata()
prod2.calculation()