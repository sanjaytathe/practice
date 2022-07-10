def forward(list1):
   n=int(input("enter the number"))
   for i in range(n):
     popElem = list1.pop(0)
     list1.append(popElem)
   print(list1)
list1=[10,20,30,40,50,60,70]
forward(list1)
