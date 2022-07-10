n=int(input("enter the no of subject"))
d={}
for i in range(n):
    name=input("enter the name of student")
    if name not in  d.keys():
     mark=int(input("enter the marks"))
     d[name]=mark
while True:
    name = input("enter  student name to get mark")

    if name not in d:
       print("student not found")
    else:
        print("the mark of", name, "are", d[name])


    option=int(input('''do you find another student mark
           1 yes
           2 no'''))
    if option==1:
        continue
    else:
        break
