'''
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
------------------------------------------------------------------------------------------------------------------------
1) identifier :- An identifier is a name having a few letter,number
                 and special character(underscore)

1) 123total x
2) total123 √
3) java2share √
4) ca$h x
5) _abc_abc_ √
6) def x
7) if x

rahul!= Rahul
rahul==rahul   #case sensitivity
---------------------------------------------------------------------------------------------------------------------------
2) keyword
In Python some words are reserved to represent some meaning or functionality. Such type
of words are called Reserved words.
There are 33 reserved words available in Python.
 True,False,None
 and, or ,not,is
 if,elif,else
 while,for,break,continue,return,in,yield
 try,except,finally,raise,assert
 import,from,as,class,def,pass,global,nonlocal,lambda,del,with
--------------------------------------------------------------------------------------------------------------------------
3) variable
:- variable is reserved memory location to store value
In python memory location depend on value
if value same the memory location will same
eg a=10
   b=10  both memory location is same
-------------------------------------------------------------------------------------------------------------------------
4)Datatype
:-Datatype represent type of data stored into a variable
1) Built in datatype
#mutable :- list,dic,set
#immutable :-  int,float,string,touple,complex
#type of casting :-int,float,string,boolean

          indexing    ordered    mutable   Duplicate
 []         /           /           /         /
 ()         /           /           x         /
 {}         x           x           /         x
 {k:v}      x           /           /         x

2) user defined datatype :- class, module
-------------------------------------------------------------------------------------------------------------------------
5) operator
1. Arithmetic Operators
2. Relational Operators or Comparison Operators
3. Logical operators
4. Bitwise oeprators
5. Assignment operators
6. Special operators

111
1. Arithmetic Operators:
+ ==>Addition
- ==>Subtraction
* ==>Multiplication
/ ==>Division operator
% ===>Modulo operator
// ==>Floor Division operator
** ==>Exponent operator or power operator

222
Relational Operators:
>,>=,<,<=

333
Logical Operators:
and, or ,not

444
Operator Description
& If both bits are 1 then only result is 1 otherwise result is 0
| If atleast one bit is 1 then result is 1 otherwise result is 0
^ If bits are different then only result is 1 otherwise result is 0
~ bitwise complement operator i.e 1 means 0 and 0 means 1
>> Bitwise Left shift Operator
<< Bitwise Right shift Operator

555
membership opearator
in,not in

666
identity opearator
is,is not
--------------------------------------------------------------------------------------------------------------------------
6)Type of casting
:- We can convert one type value to another type
:- This conversion is called Typecasting

1. int() , 2.float() , 3.complex() , 4.bool() , 5.str()
1. int()
Eg:
1) >>> int(123.987)
2) 123
5) >>> int(True)
6) 1
7) >>> int(False)
8) 0
9) >>> int("10")
10) 10
11) >>> int("10.5")
12) ValueError: invalid literal for int() with base 10: '10.5'
13) >>> int("ten")
14) ValueError: invalid literal for int() with base 10: 'ten'


2)float()
1) >>> float(10)
2) 10.0
3) >>> float(10+5j)
4) TypeError: can't convert complex to float
5) >>> float(True)
6) 1.0
7) >>> float(False)
8) 0.0
9) >>> float("10")
10) 10.0
11) >>> float("10.5")
12) 10.5
13) >>> float("ten")


3)complex()
Eg:
1) complex(10)==>10+0j
2) complex(10.5)===>10.5+0j
3) complex(True)==>1+0j
4) complex(False)==>0j
5) complex("10")==>10+0j
6) complex("10.5")==>10.5+0j
7) complex("ten")
8) ValueError: complex() arg is a malformed string


4)Boolean()
1) bool(0)==>False
2) bool(1)==>True
3) bool(10)===>True
4) bool(10.5)===>True
5) bool(0.178)==>True
6) bool(0.0)==>False
7) bool(10-2j)==>True
8) bool(0+1.5j)==>True
9) bool(0+0j)==>False


5)string()

1) >>> str(10)
2) '10'
3) >>> str(10.5)
4) '10.5'
5) >>> str(10+5j)
6) '(10+5j)'
7) >>> str(True)
8) 'True'
-------------------------------------------------------------------------------------------------------------------------
7) All datatype
1)String
string:- A string is sequence of character enclosed in single and double quote

s='This is ' single quote symbol' ==>invalid
s='This is \' single quote symbol' ==>valid
s="This is ' single quote symbol"====>valid
s='This is " double quotes symbol' ==>valid
s='The "Python Notes" by 'durga' is very helpful' ==>invalid
s="The "Python Notes" by 'durga' is very helpful"==>invalid
s='The \"Python Notes\" by \'durga\' is very helpful' ==>valid



1. len()
s="python"
print(len(s))

2.upper(),lower(),title(),Capitalize(),islower()
s="python"
print(s.upper())

3. find()
s="python is iner lanf"
print(s.find('is'))

4.isalnum(),isalpha(),isdigit()
s="python"
print(s.isalnum())

5. rstrip(),lstrip()
s=" python1"
print(s.lstrip())

6.isspace()
s=" "
print(s.isspace())

7. repalce
s="python is"
print(s.replace('is','if'))(old,new)


8.join()
s=['sanjay','tathe']
d=" ".join(s)
print(d)

9.split()
s="sanjay tathe"
d=s.split(" ")
print(d)


10. swapcase()  lower()-upper()
s="sanjay tathe"
print(s.swapcase())
--------------------------------------------------------------------------------------------------------------------------
8) List
*  Lists are used to store multiple items in a single variable
* it is an ordered sequence of ordered
* it is very flexible
* allow duplicate value
* it is one of most used datatype
* heterogeneous objects allowed

1.append,del,pop,clear,insert,extend,min,max,sort,reverse
'''

# x=[]
# y=[2,4,6,8]
# while True:
#  opr = int(input('''
#  1 append
#  3 show last element
#  4 insert
#  5 max value
#  6 min value
#  7 display all list
#  8 reverse
#  9 multiplication
#  10 clear
#  '''))
#  if opr == 1:
#          a=int(input("enter the no"))
#          x.append(a)
#          print(x)
#
#  elif opr == 2:
#     x.pop()
#     print(x)
#  elif opr == 3:
#     print("last element", x[-1])
#  elif opr == 4:
#     v=int(input("enter the np "))
#     s=int(input(" enter the positin"))
#     c = x.insert(s, v)
#     print(c)
#     print(x)
#  elif opr==5:
#      z=max(x)
#      print("maximum value is ",z)
#  elif opr == 6:
#      g =min(x)
#      print("minimum value is",g)
#  elif opr==7:
#      print(" display list",x)
#  elif opr==8:
#      x.reverse()
#      print(" reverse the list",x)
#  elif opr==9:
#      d=[x[i]*y[i] for i in range(len(x))]
#      print("multiplication of x and y",d)
#  elif opr==10:
#       x.clear()
#       print(x)
'''append,del,  pop, clear, insert,extend,remove

-------------------------------------------------------------------------------------------------------------------------------
3) Tuple
* it is immutable
* it represent in () paranthesis
* it is faster than list
* it is ordered sequence of item
* Tuples are stored in a single block of memory. Tuples are immutable so, 
It doesn't require extra space to store new objects

1)packing:- tuple packing means assigned multiple value into a tuple
eg:-
a=1
b=2
c=3
t=(a,b,c)
print(t)
2)unpacking :- tuple unpacking means splitting tuple element into
               individual variable
eg :- 
t=(1,2,3)
a,b,c=t
print(a)
---------------------------------------------------------------------------------------------------------------------------
4)Dictionary
* dictionary is unordered collection of key-value pair
* it is mutable
* key is unique we cant use same kay
* stored data as key-values pairs

All function
course = {
    'python': {'duration': '2 month', 'fees': 8000},
    'java': {'duration': '4 month', 'fees': 10000},
    'c++': {'duration': '3 month', 'fees': 6000},
}
1.get()
s=course.get('python')
print(s)  o/p:- {'duration': '2 month', 'fees': 8000}
or
print(course['python']   o/p:- {'duration': '2 month', 'fees': 8000}

2.keys()
for i in course.keys():
    print(i)     
o/p:-
python
java
c++

3.values()
for i in course.values():
    print(i)
o/p:-
{'duration': '2 month', 'fees': 8000}
{'duration': '4 month', 'fees': 10000}
{'duration': '3 month', 'fees': 6000}

4.items()
for i,j in course.items():
    print(i,j)
o\p:- 
python {'duration': '2 month', 'fees': 8000}
java {'duration': '4 month', 'fees': 10000}
c++ {'duration': '3 month', 'fees': 6000}

5.insert()
course['sanjay']={'duration':'4 month'}
for i,j in course.items():
    print(i,j)
o\p :-
python {'duration': '2 month', 'fees': 8000}
java {'duration': '4 month', 'fees': 10000}
c++ {'duration': '3 month', 'fees': 6000}
sanjay {'duration': '4 month'}

6.dict()
d=dict(name='sanjay',fees=5000)
print(d)
o\p :-
{'name': 'sanjay', 'fees': 5000}

7.del()
del course['python']
print(course)

7.pop()
course.pop('python')
print(course)

8.max and min
x={
    'physics':82,
    'math':65,
    'history':75
}
print(max(x,key=x.get))
print(min(x,key=x.get))
--------------------------------------------------------------------------------------------------------------------------
5)set
* dictionary is unordered collection of key-value pair
* it is mutable

1) union  #all element
a={1,2,3}
b={2,4}
x=a.union(b)
print(x)  o/p :- {1,2,3,4}

2)intersection  # common
a={1,2,3}
b={2,4,1}
x=a.intersection(b)
print(x)   o/p :- {1,2}

3) difference
a={1,2,3}
b={2,4,1}
x=a.difference(b)
y=b.difference(a)
print(x)   o/p :- {3}
print(y)   o/p :- {4}

1)x={1,2,3,5,6}
x.add(7)
print(x)

2)pop,update,clear,remove,discard
---------------------------------------------------------------------------------------------------------------------------
8) Format
a="sanjay {} {}".format("ganesh","tathe")
print(a)
o/p :- sanjay ganesh tathe

a=10
b=20
print(f"addition of {a}+{b}")
--------------------------------------------------------------------------------------------------------------------------
9) Indentation :- Indentation refer to space that are used in the beginning of statement
                by default python puts 4 space but it can be changed programmer
---------------------------------------------------------------------------------------------------------------------------
10) while and for loop :-
1) for loop :- 1. it is used for iteration over a sequence
               2. in for loop statement is executed then after increment/decrement the value
               3. we used for loop when we already know no of loop iteration
               4. In for loop execute n number of steps in single line
               5. if the condition not satisfy it execute infinite times
               6. syntax :
               for(initialization,condition,inc/dec)
               {
               statement;
               }
               
2)while loop :- 1. it is used to execute a block of statement repeatedly until given
               condition satisfy
               2. in while loop statement is executed then before and after increment/decrement the value
               3. we used while loop when we dont know no of loop iteration
               4. In while loop it is not possible               
               5. but in while loop if condition noy satisfy it will show compilation error
               6. syntax :-
                 while(condition)
                 {
                   statement;
                   inc/dec;
                 }
---------------------------------------------------------------------------------------------------------------------------
11) 1)if else statement
if condition :
 statement-1
else :
 statement-2
  
2) Nested if else
if condition1:
   if condition 2:
      statement 1
   else:
      statement 2
else:
statement 3
--------------------------------------------------------------------------------------------------------------------------
12) range()
:- range() function is used to generate a sequence.
   range(start,stop,stepwise)
-------------------------------------------------------------------------------------------------------------------------
13) Break and continue statement
1. Break statement :- break statement is used to jump of loop to process next statement in program
eg:- 
for i in range(10):
    if i==5:
        break
    print(i)

2.continue statement :- continue statement is used in a loop to go back to the beginning of loop
eg:- 
for i in range(10):
    if i==5:
        continue
    print(i)
--------------------------------------------------------------------------------------------------------------------------
14) pass statement
 :-  pass statement is use to do nothing
 :- it can be used inside a loop or if statement to represent no operation
--------------------------------------------------------------------------------------------------------------------------
15)pattern
1.right pattern
n=int(input("enter the number rows"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

2.inverse right pattern
for i in range(n+1,0,-1):
    for j in range(1,i+1):
    
3.left pattern
for i in range(n+1):
    for j in range(n - i):
        print(" ", end=" ")
    for x in range(i):
        print("*", end=" ")
        
3.right with number
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+1
        
4.tri pattern
for i in range(n):
    for j in range(0,n-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
---------------------------------------------------------------------------------------------------------------------------
16)general
 1. dynamic list :- user input
 2. static list :- direct define
-------------------------------------------------------------------------------------------------------------------------
17) ASCII
:- american standard code for information interchange
 A-Z = 65-90
 a-z = 97-122
 0-9 =48-57
 
print(chr(69))
print(chr(101))
print(ord(8)).
--------------------------------------------------------------------------------------------------------------------------
18)
1. del :- delete the element from element by indexing
x=[10,20,30,10,20]
del x[2]
print(x)

2. pop :- return the element.remove last element
x=[10,20,30,10,20]
x.pop()
print(x)

3. remove :- it works on value
x=[10,20,30,10,20]
x.remove(20)
print(x)
-------------------------------------------------------------------------------------------------------------------------
19) frozen set & set
:- both are same but frozen set are immutable
x={1,2,3,5,6}
t=frozenset(x)
print(type(t))
t.add(8)
print(t)
------------------------------------------------------------------------------------------------------------------------ 
what is string slicing??
:- Python slicing is about obtaining a sub-string from the given string by slicing
   it respectively from start to end.
x="sanjaytathe"
print(x[:9:2])  
--------------------------------------------------------------------------------------------------------------------------
21) definition
1) list:- list is the on of the datatype,it is mutable,changeable,ordered sequence 
         :- it is used to store multiple item in a single variable

2) dictionary:- dictionary are used to store data value in key : values pairs
              :- don't allow duplicate
-------------------------------------------------------------------------------------------------------------------------
22) it is possible tuple comprehension ??
x=(x*x for x in range(10))
print(next(x))
print(next(x))
print(next(x)) 
-------------------------------------------------------------------------------------------------------------------------   
   
   
    
'''

