x=[]
name=input("enter the student name: - ")
sub=int(input("enter the no of subject"))
sum=0
for i in range(sub):
    marks=int(input("enter the marks"))
    x.append(marks)
    sum=sum+marks
    avg=sum/sub
print(x)
print(sum)
print(avg)
if min(x)<35:
    print("fail")
else:
    print("pass")