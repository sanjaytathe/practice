'''
Python's Object Oriented Programming (OOPs)
111.What is Class:
⚽ In Python every thing is an object. To create objects we required some Model.

2.How to Define a class?
We can define a class by using class keyword

333.There are 3 types of variables are allowed.
1. Instance Variables (Object Level Variables)
:- instance variable are the variables whose seperate copy is created in every object
2. Static/class Variables (Class Level Variables)
:- A class variable that is shared by all instance of a class
:-class variable define within a  class and outside the method
3. Local variables (Method Level Variables

Note:
1. self should be first parameter inside constructor
 def __init__(self):

class abc:
a=10     # class variable
def fun(self,a) #local variable
self.a=20  #instance variable
--------------------------------------------------------------------------------------------------------------------------
2) four pillar of oops (principle)
1.Encapsulation
2.Abstraction
3.Inheritance
4.polymorphism

1)Encapsulation
:- combination of data and method that work on that data within one unit
class car:
    def drive(self):
        print("driving")
    def __drive1(self):
        print("driving1")
o=car()
o.drive()
o.__drive1()
:- we can't call private method in outside class


2) Abstraction
:- Design may be complex keep interface simple
:- allow only very important method to be visible
:-  hides the unnecessary umethod from the user.

3) inheritance
use the existing class design & add something new

4) polymorphism :-  Polymorphism simply means having many forms
:- polymorphism is the ability of an object to take on many forms
--------------------------------------------------------------------------------------------------------------------------
3)self variable
* self is a default variable that contain memory address of current object
* This variable is used to refer all the instance and method
* We can access local variable into other method
-------------------------------------------------------------------------------------------------------------------------
5)overloading and overriding
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
    def result(self,a,b):
        print(a+b)
    def result(self,a,b):
        print(a-b)
    def result(self,a,b):
        print(a*b)
s=A()
s.result(10,5) o/p :- 50

class A:
    def abc(self,x=10,y=20,z=30):
        print("sum of :-",x+y+z)
o=A()
o.abc()          o/p :- 60
o.abc(15)            :- 65
o.abc(20,30,40)      :- 90

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
--------------------------------------------------------------------------------------------------------------------------
5)How to delete instance variable from the object:
1) class Test:
2) def __init__(self):
3) self.a=10
4) self.b=20
5) self.c=30
6) self.d=40
7) def m1(self):
8) del self.d
9)
10) t=Test()
11) print(t.__dict__)
12) t.m1()
13) print(t.__dict__)
14) del t.c
15) print(t.__dict__)
Output
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
{'a': 10, 'b': 20, 'c': 30}
{'a': 10, 'b': 20}
--------------------------------------------------------------------------------------------------------------------------
6) constructor :-python support special type of method called
             constructor for initializing the instance variable of class

 Object :- Object is a class type variable or class instance.
--------------------------------------------------------------------------------------------------------------------------
7) type of inheritance class
inheritance :- inheritance allow us define a class that inherit all the method and properties from another class
 1. single level inheritance
 :- Single-level inheritance enables a derived class to inherit characteristics from a single-parent class
 2. multilevel inheritance
 :-  Multi-level inheritance enables a derived class to inherit properties from an immediate parent
     class which in turn inherits properties from his parent class.
 3. multiple inheritance
 :- Multiple level inheritance enables one derived class to inherit properties from more than one base class.
 4. hierarchical inheritance
 :- Hierarchical level inheritance enables more than one derived class to inherit properties from a parent class.
 5. hybrid inheritance
 :- Hybrid inheritance is a combination of multiple inheritance and multilevel inheritance
 ------------------------------------------------------------------------------------------------------------------------
 11) what is class and method??
:- class is nothing but collection of object

object:- object is instance of class that execute the class

method :- a method is collection of statement that are grouped together to perform an operation

pre defined function:- print,max,del,min,
-------------------------------------------------------------------------------------------------------------------------
12) what is oops ??
:- oops is a programming language model organised  around object rather than action
----------------------------------------------------------------------------------------------------------------------------
13) what is MRO??



:- (method resolution order)
:- search for the child class before going to its parent class
:- when class is inherited from several classes, it search in the order from
  left to right in the parent class
-------------------------------------------------------------------------------------------------------------------------







'''