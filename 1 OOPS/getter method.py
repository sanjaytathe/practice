class student:
    def san(self,name):
        self.name=name
    def gan(self):
        return self.name
    def tan(self, mark):
        self.mark = mark
    def pan(self):
        return self.mark

s=student()
n=int(input("enter the no"))
for i in range(n):
    name=input("enter name")
    s.san(name)
    mark=int(input("enter the marks"))
    s.tan(mark)
print("hi",s.gan())
print('your mark',s.pan())




#
# class student:
#     def san(self,name):
#         self.name=name
#     def gan(self):
#         return self.name
#     def tan(self, mark):
#         self.mark = mark
#     def pan(self):
#         return self.mark

# s=student()
# n=int(input("enter the no"))
# try:
#     if n==0:
#         print("YES")
# except Exception as e:
#     print(e)
# for i in range(n):
#     name=input("enter name")
#     s.san(name)
#     mark=int(input("enter the marks"))
#     s.tan(mark)
# print("hi",s.gan())
# print('your mark',s.pan())
# except:
#        print("no")