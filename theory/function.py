'''
1) Defination
:- we can define function using def keyword followed by function name and  paranthesis
:- A function is a block of statement which can used by repeatatively in program
:- def represent starting of function definition
-------------------------------------------------------------------------------------------------------------------------
2) Advantage
* Write once and use it many times as you need
* divide large task into many small task it will help you debug code
* you can add or remove new feature to a function anytime

**-syntax:
 def function_name(parameter):
   function body
   return

** Calling a function
 A function runs when we call,function can't run on its own

** Python supports 2 types of function

1.built in function
ex:- print()
eval()
type()
id()

2 user defined function
Syntax to create user defined functions:
def function_name(parameters) :
 """ doc string"""
 ----
 -----
 return value

** Return Statement:
Function can take input values as parameters and executes business logic, and returns
output to the caller with return statement
--------------------------------------------------------------------------------------------------------------------------
3). type of argument
1. positional arguments
2. keyword arguments
3. default arguments
4. Variable length arguments

1.positional arguments
 These are the arguments passed to function in correct positional order.
def sub(a,b):
 print(a-b)
sub(100,200)
sub(200,100)

2. keyword arguments
We can pass argument values by keyword i.e by parameter name.
Eg:
 def wish(name,msg):
 print("Hello",name,msg)
 wish(name="Durga",msg="Good Morning")
 wish(msg="Good Morning",name="Durga")

 Output
 Hello Durga Good Morning
 Hello Durga Good Morning


 3. Default Arguments:
Sometimes we can provide default values for our positional arguments.
Eg:
 def wish(name="Guest"):
 print("Hello",name,"Good Morning")

 wish("Durga")
 wish()

 Output
 Hello Durga Good Morning
 Hello Guest Good Morning


4 variable lenght parameter
:- when you are not clear how many argument you need to pass to a particular function
   then we use *arg and *kwargs

:- kwargs keyword are used to stored in dictionary
Eg:
def display(**kwargs):
 for k,v in kwargs.items():
 print(k,"=",v)
 display(n1=10,n2=20,n3=30)
 display(rno=100,name="Durga",marks=70,subject="Java")

 Output
 n1 = 10
 n2 = 20
 n3 = 30
 rno = 100
 name = Durga
 marks = 70
 subject = Java
 -------------------------------------------------------------------------------------------------------------------------
4)Types of Variables
Python supports 2 types of variables.
1. Global Variables
2. Local Variables

1. Global Variables
The variables which are declared outside of function are called global variables.
These variables can be accessed in all functions

2. Local Variables:
The variables which are declared inside a function are called local variables.
Local variables are available only for the function in which we declared it.i.e from outside
of function we cannot access
-------------------------------------------------------------------------------------------------------------------------
5). Recursive Functions
A function that calls itself is known as Recursive Function.
def abc(x):
    if x==0:
        fact=1
    else:
        fact=x*abc(x-1)
    return fact
fact=abc(5)
print(fact)
-------------------------------------------------------------------------------------------------------------------------
6. anonymous function
:-In Python, an anonymous function is a function that is defined without a name
:- A function without a name is called as lambda function
1.lambda Function:
We can define by using lambda keyword
lambda n:n*n
Syntax of lambda Function:
lambda argument_list : expression

sum=lambda a,b:a+b
print(sum(10,2))

fact=lambda i:1 if i==0 else i*fact(i-1)
print(fact(5))

2.filter() function:
We can use filter() function to filter values from the given sequence based on some
condition.
filter(function,sequence)

val=[1,2,3,4,5,6,7,8,9]
d=list(filter(lambda a:a%2==0,val))
print(d)

# def evenodd(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# list1=[2,3,4,5,6,7,8]
# result=list(filter(evenodd,list1))
# print(result)

3.map() function:
For every element present in the given sequence,apply some functionality and generate
new element with the required modification. For this requirement we should go for
map() function.
Eg: For every element present in the list perform double and generate new list of doubles.
Syntax:
map(function,sequence)

# num=[2,4,6,8]
# add=map(lambda n:n*n,num)
# print(list(add))

4.reduce() function:
reduce() function reduces sequence of elements into a single element by applying the
specified function.
reduce(function,sequence)

from functools import reduce
n=[1,5,2,3,4,5,3]
# z=reduce(lambda a,b:a+b,n)
# print(z)
-------------------------------------------------------------------------------------------------------------------------

777.Nested Functions:
We can declare a function inside another function, such type of functions are called Nested
functions.
-------------------------------------------------------------------------------------------------------------------------
888
 what is decorator??
:- decorator means a function that takes another function as its argument, and returns yet another function
or
:- Extend the functionality of existing function without modifying them
def decor2(num):
    def inner():
        a=num()
        d=a+5
        return d
    return inner
@decor2
def decor1():
    a=10
    return a
print(decor1())

decorator chaining :- applying more than one decorator inside a function
--------------------------------------------------------------------------------------------------------------------------
8) What is generator??
:- generator are function that return a sequence of value
:- we use yield function to return value from function

yield :-yield statement return the element from a generator function into generator object

def abc(x):
    a=1
    while a<=x:
        yield a
        a=a+1
values=abc(10)
print(next(values))
print(next(values))
--------------------------------------------------------------------------------------------------------------------------
'''