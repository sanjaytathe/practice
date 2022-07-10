class employee:
    def inputdata(self):
        self.__em_no=int(input("enter employee no"))
        self.__em_name=input("enter employee name")
        self._salary=int(input("enter employee salary"))
class manager(employee):
    def calculation(self):
        self.__pf=(self._salary)*0.10
        self.__netsalary=self._salary-self.__pf
        print("pf is =",self.__pf)
        print("net salary is =", self.__netsalary)
emp=manager()
emp.inputdata()
emp.calculation()



# class employee:
#     def inputdata(self):
#         self.__em_no=int(input("enter employee no"))
#         self.__em_name=input("enter employee name")
#         self._salary=int(input("enter employee salary"))
# # class manager(employee):
#     def calculation(self):
#         self.__pf=(self._salary)*0.10
#         self.__netsalary=self._salary-self.__pf
#         print("pf is =",self.__pf)
#         print("net salary is =", self.__netsalary)
# emp=employee()
# emp.inputdata()
# emp.calculation()