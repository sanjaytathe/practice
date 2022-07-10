z= lambda x,y,opr:x+y if opr=='+' else x-y if opr=='-' else x*y if opr=='*' else x/y if opr=='/' else " No such operator found"
x,opr,y= input(" perform your task : ").split(" ")
print(z(int(x),int(y),opr))

val=[1,2,3,4,5,6,7,8,9]
d=list(filter(lambda a: a%2!=0,val))
print(d)