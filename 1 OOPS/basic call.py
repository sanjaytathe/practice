class vehicle:
    def __init__(self,model,price,milage):
       self.model=model
       self.price=price
       self.milage=milage
    def show(self):
        print(self.model)
        print(self.price)
        print(self.milage)
c1=vehicle(2011,25000,53)
c1.show()