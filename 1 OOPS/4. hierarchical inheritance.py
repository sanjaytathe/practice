class student:
    def input_data(self):
        self.__name=input("enter the student name")
        self.__roll=int(input("enter the roll no"))
        self._mark1=(int(input("enter the marks 1: ")))
        self._mark2=int(input("enter the marks 2: "))
        self._mark3=int(input("enter the marks 3: "))
class btech(student):
    def result(self):
        self.__tm=self._mark1+self._mark2+self._mark3
        print(self.__tm)
class mbbs(student):
    def result(self):
        self.__tm=self._mark1+self._mark2+self._mark3
        print(self.__tm)
c=btech()
c.input_data()
c.result()
d=mbbs()
d.input_data()
d.result()