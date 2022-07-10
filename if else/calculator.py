num1=int(input("enter the value 1 :- "))
num2=int(input("enter the value 2 :- "))
oprator=input('''enter the operator :-
           + addition
           - subtraction
           / division
           * multiplication
           ** power of  ''')
if oprator=="+":
   print("addition of num1 and num2 is ",num1+num2)
elif oprator=="-":
   print("subtraction of num1 and num2 is ",num1-num2)
elif oprator=="/":
   print("division of num1 and num2 is ",num1/num2)
elif oprator=="*":
   print("multiplication of num1 and num2 is ",num1*num2)
elif oprator=="**":
   print("num1 to the power num2 ",num1**num2)
else:
    print("invalid operation")
