class student:
    def msg1(self):
        print("hello")
class cs(student):
    def msg2(self):
        print("welcome")
class ce(student):
    def msg3(self):
        print("to")
class college(cs,ce):
    def msg4(self):
        print("nagpur")
d=college()
d.msg1()
d.msg2()
d.msg3()
d.msg4()