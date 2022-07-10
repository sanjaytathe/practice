'''
1) what is palindrome number??
:- palindrome number is a number that  remain same when digits are reversed
:- which string spelling is unchanged when letter reversed
if s==s[::-1]:
-------------------------------------------------------------------------------------------------------------------------
2) what is armstrong number??
:- the sum of cube of each digit is equal to number itself
n=int(input("enter number to check for armstrong :- "))
orig=n
sum=0
while(n>0):
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
if orig==sum:
    print("Number is armstrong")
else:
    print("Number is not armstrong")
-------------------------------------------------------------------------------------------------------------------------
3) what is decorator??
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
4) what is garbage collection??
:- garbage collection is to release memory when the object is no longer in use
a=10
a=20
print(a)=20
10 is  garbage collection
----------------------------------------------------------------------------------------------------------------------------
5) what is inheritance??
:- in
class Abc:
    def __init__(self):
        pass
    def method1(self):
        print("this is method of Abc")
class Bcd(Abc):
    def __init__(self):
        pass
    def method2(self):
        print("this is method ofBcd")
obj=Bcd()
obj.method1()
obj.method2()
--------------------------------------------------------------------------------------------------------------------------
6) what is exception handling??
:- python provides a way to handle the exception so that code can be executed without any interruption
try:
    d=10/0
    print(d)
except Exception as w:
    print(w)
print("welcome")
--------------------------------------------------------------------------------------------------------------------------
7) what is function??
:- :- we can define function using def keyword followed by function name and  paranthesis
:- A function is a block of statement which can used by repeatatively in program
:- def represent starting of function definition
def sum(x,y):
    d=x+y
    print(d)
sum(2,5)
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
-------------------------------------------------------------------------------------------------------------------------
9) feature of python ??
:-  Python was developed by Guido Van Rossam in 1989 while working at National
Research Institute at Netherland.

python :- python is a high programming ,interpreted & object oriented language
feature:=
1) Python is a general purpose high level programming language.
:- High level language is created for developing user-friendly software and program
:- it enables people to write program easily in english
:- this language require a compiler and interpreter to translate the program into machine code

2) simple easy to learn
:- python is simple programming language . when we read programme we can feel like
   reading english statement and syntax are very simple compared to other language

3) Interpreted Language
:- it scans the code line by line
:- interpreter show one error at a time
: -execution time is more

4) Portability:
:- Python programs are portable. ie we can migrate from one platform to another platform
   very easily. Python programs will provide same results on any platform.

5) Platform Independent:
:- Once we write a Python program,it can run on any platform without rewriting once again.

6) Both Procedure Oriented and Object Oriented programming:
:- Python language supports both Procedure oriented  and object oriented language.
   we can use of class and object in python

7) exception handling
:- python provides a way to handle the exception so that code can be executed without any interruption

8)  Dynamically Typed:
:-   In Python we are not required to declare type for variables. Whenever we are assigning
    the value, based on value, type will be allocated automatically.Hence Python is considered
    as dynamically typed language
-------------------------------------------------------------------------------------------------------------------------
10) what is memory management ?
:- private heap containing python object and data structure
:- Built in garbage collector recycled all unused memory
------------------------------------------------------------------------------------------------------------------------
11) what is class and method??
:- class is nothing but collection of object

object:- object is instance of class that execute the class

method :- a method is collection of statement that are grouped together to perform an operation

pre defined function:- print,max,del,min,
------------------------------------------------------------------------------------------------------------------------
12) How to exit from the loop?
:- with the help of break statement you can exit from the loop.
------------------------------------------------------------------------------------------------------------------------
13) How to skip some iteration from the loop?
:- with the help of continue  statement you can exit from the loop.
------------------------------------------------------------------------------------------------------------------------
14)  When else part will be executed in loop??
:- The else part gets executed only if the loop has completed its execution fully without hitting a break statement
 for i in range(1,4):
    print(i)
else:
    print("hi")
it will execute
------------------------------------------------------------------------------------------------------------------------
15) How to create dictionary??
:- In Python, a dictionary can be created by placing a sequence of elements within curly {} braces, separated by 'comma'
s={"sanjay":100,"tathe":200}
-------------------------------------------------------------------------------------------------------------------------
16)  How to delete element from dictionary?
:-  you can delete element from dictionary by using del() function

del()
del course['python']
print(course)
-------------------------------------------------------------------------------------------------------------------------
17) deep copy and shallow copy
1)deep copy :-
* in deep copy any changes made to a copy of object do not reflect in the original object
import copy
l=[[1,2],[3,4]]
cp=copy.deepcopy(l)
cp[0][0]=42
print(cp)
print(l)

2) shallow copy
*  in shallow copy any changes made to a copy of object  reflect in the original object
import copy
l=[[1,2],[3,4]]
cp=copy.copy(l)
cp[0][0]=42
print(cp)
print(l)
-------------------------------------------------------------------------------------------------------------------------
oops:- oops is a type of programming which is based on object rather than function and procedure
18) what is the principle of oops
:- 2) four pillar of oops (principle)
1.Encapsulation
2.Abstraction
3.Inheritance
4.polymorphism

1)Encapsulation
:- combination of data\variable and method that work on that data
class car:
    def drive(self):
        print("driving")
    def __drive1(self):
        print("driving1")
o=car()
o.drive()
o.__drive1()
:- we can't call private method in outside class
:=we can't modify private variable in outside the class


2) Abstraction
:- Design may be complex keep interface simple
:- allow only very important method to be visible

3) inheritance
use the existing class design & add something new

4) polymorphism :-  many forms
:- polymorphism means same function name being uses for different type
:- polymorphism is the ability of an object to take on many forms
overloading and overriding
1)overloading :- when more one method with the same name
               is defined in the same class it is known
               as overloading
eg :-
class A:
    def abc(self,*x):
        print("sum of :-",sum(x))
o=A()
o.abc()        o/p:-0
o.abc(10)         :-10
o.abc(20,30,40)   :-90

class A:
    def abc(self,x=10,y=20,z=30):
        print("sum of :-",x+y+z)
o=A()
o.abc()          o/p :- 60
o.abc(15)            :- 65
o.abc(20,30,40)      :- 90

class car:
    __a=100
    def drive(self,x,y):
      print(x+y)
    def drive(self,x,y):
        print(x*y)
o=car()
o.drive(10,12)



2)overriding :- if we write method in the both classes parent and child class
                parent class method is not available to the child class

             :- method overriding is used when programmer want to modify or existing
                behavior of method
eg :-
class add:
    def result(self,a,b):
        print(a+b)
class mul(add):
    def result(self,a,b):
        print(a*b)
m=mul()
m.result(10,20) o\p = 200
-------------------------------------------------------------------------------------------------------------------------
19) what is file handling??
:- The process of working with files is called file handling
:- opening a file
:- performing a some task
:- closing a file
:- it is used for store permanent file

# a=open("sanjay.txt",'w')
# a.write("rohit sharma")
# a.close()

txt file:- stored data in the form of character.
           it is used to stored data and string
------------------------------------------------------------------------------------------------------------------------
20) what is lambda ??
:- A function without a name is called as lambda function
:- A lambda function can take any number of argument but only have a expression
:- lambda is an anonymous function in python

syntax:- lambda argument:expression
eg:-
sum=lambda x,y:x+y
print(sum(2,5))
------------------------------------------------------------------------------------------------------------------------
21) what is filter ??
:-Python's filter() is a built-in function that allows you to process
 an iterable and extract those items that satisfy a given condition
syntax:- filter(function_name,iterable)
x=[1,2,3,4,5]
def san(n):
    if n%2==0:
        return True
    else:
        return False
c=list(filter(san,x))
print(c)
-------------------------------------------------------------------------------------------------------------------------
22) what is map??
:- this function execute a specified function on each element of the iterable
syntax:- map(function_name,iterable)
x=[1,2,3,4,5]
c=list(map(lambda n:n*n,x))
print(c)
-------------------------------------------------------------------------------------------------------------------------
23) difference between list comprehension and dic comprehension??
:- list comprehension represent creation of new list from an iterable object
syntax:- [expression for item in iterable_obect]
y=[1,2,3,4,5]
t=[x*x for x in y ]
print(t)

dic comprehension
syntax:-
{key:value for (key:value) in iterable if conditional}
dic1={n:n*2 for n in range(10)}
print(dic1)

dic1={n:n*2 for n in range(10) if n%2==0}
print(dic1)
-------------------------------------------------------------------------------------------------------------------------
24) what is list and tuple??
:- list and tuple are both sequence datatype that can store a collection of object.
   list is mutable and tuple is immutable
   tuple consume less energy than list
-------------------------------------------------------------------------------------------------------------------------
25) what is __init___??
:- __init__ is a constructor method in python and is automatically called when new object is created
------------------------------------------------------------------------------------------------------------------------
26) How memory managed in python??
:- Memory management in python involve a private heap containing all type of object structure
:- the allocation of heap space for python object is done by python memory manager
:- python also has a built in garbage collector which recycle all the unused memory
-------------------------------------------------------------------------------------------------------------------------
27) what is difference generator and iterator??
:= * every generator is an iterator
   * every iterator is not a generator

:- * generator are iterator which can execute only once
   * an iterator is an object which contain a countable no of values and it is uses to
   iterate over iterable object list,tuple
-------------------------------------------------------------------------------------------------------------------------
28) what is difference between module and package in python??
:-
module :- the module is a simple python file that contain collection of function and global variable
          and with having a.py extension file

packages :- the package is a simple directory having collection of module
------------------------------------------------------------------------------------------------------------------------
29) what is 'self' keyword in python??
:- the 'self' parameter is a reference to the current instance of the class and is use to access variable
   that belong to the class
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name)
        print(self.age)
o=Person('sanjay',24)
o.info()
------------------------------------------------------------------------------------------------------------------------
30) whats are *arg and *kwargs
:- when you are not clear how many argument you need to pass to a particular function
   then we use *arg and *kwargs
eg:- *arg
def fun(*n):
   total=0
   for i in n:
       total=total+i
   print("sum",total)
fun()
fun(10)
fun(10,20,30)

eg:- **kwarg
def display(**kwargs):
 for k,v in kwargs.items():
 print(k,"=",v)
 display(n1=10,n2=20,n3=30)

*args :- it is used to add together the value of multiple argument

**kwarg :- kwargs keyword are used to stored in dictionary
-------------------------------------------------------------------------------------------------------------------------
31) what is file handling ?? different ways to read and write in file in python??
file handling :- The process of working with files is called file handling. File handling
                 concepts of Python is easy to learn and understand.
eg:- # a=open("sanjay.txt",'w')
# a.write("rohit sharma")
# a.close()

# a=open("sanjay.txt",'r')
# z=a.read()
# print(z)

:-
1) read only (r):- open text file for reading file
2) write only (w):- open text file for writing file
3) read and write (r+):- open text file for reading and writing  file
4) write and read (w+):- open text file for writing and reading file
5) append only (a) :- open text file for writing file
6) append and read (a+):- open text file for reading and writing  file
-------------------------------------------------------------------------------------------------------------------------
32) python 2.0 vs 3.0??

2.0 :- print"hello"
3.0 :- print("hello")

2.0 :- release date 2000
3.0 :- 2008

2.0 :- when teo integer are divided you always provide integer value
3.0 :- float value

2.0 :- syntax comparatively difficult
3.0 :- easy
-------------------------------------------------------------------------------------------------------------------------
33) what is pip ??
:- python pip is the package manager for python packages.
:- we can use pip to install packages  that do not come with python
syntax :- pip install package_name
------------------------------------------------------------------------------------------------------------------------
34) where python is used??
* web application
* desktop application
* machine learning
* database application
*game and many more
-------------------------------------------------------------------------------------------------------------------------
.
35)
 8) logging:- logging is useful to track the error or exception or information.
            it also help in debugging
from logging import *
basicConfig(filename="mylog.log",level=DEBUG,filemode='w',format='%(asctime)s %(message)s -%(lineno)d')
info("this is information")
warning("this is warning")
error("this is error")
-------------------------------------------------------------------------------------------------------------------------
9) how to download virtual environment
1. pip install virtualenv
2.virtualenv --python=C:\Users\Asus\AppData\Local\Programs\Python\Python310\python.exe D:\python\ev1
3.restart command prompt
4.C:\Users\Asus>D:\python\ev1\Scripts\activate.bat
5.if you want to out from virtual env then type deactivate
-------------------------------------------------------------------------------------------------------------------------
10) regular expression
:-A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
  RegEx can be used to check if a string contains the specified search pattern.
1. [abc]===>Either a or b or c
2. [^abc] ===>Except a and b and c
3. [a-z]==>Any Lower case alphabet symbol
4. [A-Z]===>Any upper case alphabet symbol
5. [a-zA-Z]==>Any alphabet symbol
6. [0-9] Any digit from 0 to 9
7. [a-zA-Z0-9]==>Any alphanumeric character
8. [^a-zA-Z0-9]==>Except alphanumeric characters(Special Characters)
9.^[a-z]==> start with Any Lower case alphabet symbol


\d :- for integer eg([0-9]=\d
\D :- for alphabets
$ :- search from back
\w :- search in string \ [a-zA-Z0-9]
sensitive :- flags=re.I

[]	A set of characters	"[a-m]"
\	Signals a special sequence (can also be used to escape special characters)	"\d"
.	Any character (except newline character)	"he..o"
^	Starts with	"^hello"
$	Ends with	"planet$"
*	Zero or more occurrences	"he.*o"
+	One or more occurrences	"he.+o"
?	Zero or one occurrences	"he.?o"
{}	Exactly the specified number of occurrences	"he.{2}o"
|	Either or	"falls|stays"
()	Capture and group


1)findall
2)search print(x.start())
3)split
4) sub
5)finditer

-------------------------------------------------------------------------------------------------------------------------
11) JSON file (javascript object notation)
:- it is mainly used for storing and transferring data between the browser and the server
json support :- array,string.number,object

* dumps :- dic (python object)to json string
* loads :- json string to dic (python object)
* dump :-  dic (python object)to json file
* load :- json file to dic (python object)

define :-  a standard text-based format for representing structured data based on JavaScript object syntax

1):- dic to json string
import json
d={
    "sanjay":3000,
    "tathe":5000
}
t=json.dumps(d)
print(type(t))
print(t)

2) json to dic
import json
d='{"sanjay":3000,"tathe":5000}'
t=json.loads(d)
print(type(t))
print(t)

3)read()
import json
file=open("sanjay.json","r")
x=file.read()
finaldata=json.loads(x)
print(finaldata);

4) json to list
import json
d='["sanjay","tathe"]'
print(type(d))
t=json.loads(d)
print(type(t))
print(t)

---------------------------------------------------------------------------------------------------------------------------
12) multi threading
:- thread is a separate flow of execution.every thread has a task

syntax:-
x=Thread(target=function_name,args=(arg1,arg2,..)

uses:-
1) multimedia graphic
2) animation
3)video games
4)web and application server

from threading import *
def twice(num):
    for i in num:
        print(2*i)
def display(num):
    for x in num:
        print(x*x)
num=[1,2,3,4,5]
t1=Thread(target=twice,args=(num,))
t2=Thread(target=display,args=(num,))
t1.start()
t1.join()
t2.start()
-------------------------------------------------------------------------------------------------------------------------
13) what is MRO??
:- (method resolution order)
:- MRO is a concept used in inheritance. It is the order in which a method
   is searched for in a classes hierarchy and is especially useful in Python
    because Python supports multiple inheritance.

--------------------------------------------------------------------------------------------------------------------------
14) pickling :- pickling refer to the process of converting the structure
               dic to byte before writing the file

unpickling :- byte to original structure
--------------------------------------------------------------------------------------------------------------------------
15) what is pip??
:- pip is a package installer for python
:- pip is a standard package manager used to install and maintain packages for Python.
------------------------------------------------------------------------------------------------------------------------





'''

