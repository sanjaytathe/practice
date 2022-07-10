class company:
    def class1(self):
        self.__emno=(int(input("enter the no")))
        self.__emname=input("enter employee name")
        self._salary=int(input("enter the value"))
class allowance(company):
    def class2(self):
        super().class1()
        self._hra=self._salary*0.24
        self._dra=self._salary*0.30
        print(self._hra)
        print(self._dra)
class employee(allowance):
    def class3(self):
        super().class2()
        self.__gross=self._salary+self._hra+self._dra
        print(self.__gross)
c=employee()
# c.class1()
# c.class2()
c.class3()