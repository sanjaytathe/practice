no=int(input("enter the number no till what you want the series: - "))
num1=0
num2=1
num3=0

while num3<=no:
    print(num3)
    num1=num2
    num2=num3
    num3=num1+num2
