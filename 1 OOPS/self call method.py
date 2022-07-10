# class A:
#     def abc(self):
#         print("my name sanjay")
# class B:
#     def mnr(self):
#         self.z=A()
#         self.z.abc()
#         print("my father name is ganesh")
# obj=B()
# obj.mnr()



class A:
    def abc(self):
        print("my name sanjay tathe")
class B(A):
    def mnr(self):
        super(B,self).abc()
        print("my father name is ganesh")
obj=B()
obj.mnr()