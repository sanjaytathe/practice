class student:
    def class1(self):
        self._mark1=(int(input("enter the marks 1: ")))
        self._mark2=int(input("enter the marks 2: "))
        self._mark3=int(input("enter the marks 3: "))
class cricket():
    def class2(self):
        self._score1=int(input("enter the score 1: "))
        self._score2=int(input("enter the score 2: "))

class total(student,cricket):
    def class3(self):
        super().class1()
        super().class2()
        self.__tm=self._mark1+self._mark2+self._mark3
        self.__ts=self._score1+self._score2
        print(self.__tm)
        print(self.__ts)
c=total()
# c.class1()
# c.class2()
c.class3()
#
#
# class Father:
#     def __init__(self):
#         print("father classs constructor")
#     def showF(self):
#         print("father class method")
# class Mother:
#     def __init__(self):
#         print("mother classs constructor")
#     def showM(self):
#         print("mother class method")
# class Son(Father,Mother):
#     def __init__(self):
#         super().__init__()
#         print("son classs constructor")
#     def showS(self):
#         print("son class method")
# d=Son()
#

















