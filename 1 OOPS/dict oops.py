# class Employee:
#
#  def __init__(self):
#    self.eno=100
#    self.ename='Durga'
#    self.esal=10000
#
# e=Employee()
# print(e.__dict__)



class test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
    def gh(self):
        del self.b
c=test()
c.gh()
print(c.__dict__)