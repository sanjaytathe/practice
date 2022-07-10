'''
1)  what is exception handling??
:- python provides a way to handle the exception so that code can be executed without any interruption

need of exception handling :-
* when an exception occur, the program terminate suddenly
* suddenly termination of program may corrupt the program
* exception may cause data loss from the file

Except :- the except block is used to catch an exception that raised in try blocked
          there can be multiple except block for try block

else :- this block will get executed when no exception is raised. Else block will execute after try block

finally :- this block will get executed of whether there is exception or not
try:
    c=a/b
    print(c)
    print("i am sanjay")
except Exception as e:
    print(e)
else:
    print("i am tathe")
finally:
    print("welcome")

Zero division error :- 10/0
name error :- when name not defined
type error :- ("10"+10)
value error :- a=int(input("enter the value")  a=hello
index error :- l=[1,2,3,4]  print(l[4])
-------------------------------------------------------------------------------------------------------------------------
19) what is file handling??
:- The process of working with files is called file handling

file :- file is the collection of data that is available to a program

advantage :-
* stored data is permanent unless someone remove it
* stored data can be shared
* it is possible to update

type of file :-
1. text file :- it stored data in the form of character.

2. binary file :- it stored data in the form of byte
                 it is used to stored text, images, pdf, audio

:- opening a file
:- performing a some task
:- closing a file
:- it is used for store permanent file

# a=open("sanjay.txt",'w')
# a.write("rohit sharma")
# a.close()

# a=open("sanjay.txt",'r')
# z=a.read()
# print(z)

1) read only (r):- open text file for reading file
2) write only (w):- open text file for writing file
3) read and write (r+):- open text file for reading and then writing  file
4) write and read (w+):- open text file for writing and then reading file
5) append only (a) :- open text file for appending file
6) append and read (a+):- open text file for appending and then reading  file
-----------------------------------------------------------------------------------------------------------------------------
3) deep copy and shallow copy
1)deep copy :-
* in deep copy any changes made to a copy of object do not reflect in the original object
* Deep copy is a process in which the copying process occurs recursively
import copy
l=[[1,2],[3,4]]
cp=copy.deepcopy(l)
cp[0][0]=42
print(cp)  o/p :- [[42, 2], [3, 4]]
print(l)   o/p :- [[1, 2], [3, 4]]

2) shallow copy
*  in shallow copy any changes made to a copy of object  reflect in the original object
* create a new object which store the reference of the original element
import copy
l=[[1,2],[3,4]]
cp=copy.copy(l)
cp[0][0]=42
print(cp) o/p :- [[42, 2], [3, 4]]
print(l)  o/p :- [[42, 2], [3, 4]]

l1=[1,2,3,4,5]
l2=l1
l2.append(7)
print(l2)  o/p :- [1, 2, 3, 4, 5, 7]
print(l1)  o/p :- [1, 2, 3, 4, 5, 7]

* do not reflect in single list
import copy
l1=[1,2,3,4,5]
l2=copy.copy(l1)
l2.append(8)
print(l2) o/p :- [1,2,3,4,5,8]
print(l1) o/p :- [1,2,3,4,5]
--------------------------------------------------------------------------------------------------------------------------------
4) logging:- logging is useful to track the error or exception or information.
            it also help in debugging
from logging import *
s='{asctime}s ** {name} ** {message}s ** {lineno}d'
basicConfig(filename="logfile1.log",level=DEBUG,filemode='w',style='{',format=s)

logger=getLogger("sanjay")
logger.debug("this is debug")
logger.info("this is info")
logger.warning("this is warning")
error("this is error")
critical("this is critical")

debug- 10
info-20
warning-30
error-40
critical-50


from logging import *
basicConfig(filename="logfile2.log",level=DEBUG,format='%(asctime)s--%(message)s')
num1=int(input("enter the value 1 :- "))
num2=int(input("enter the value 2 :- "))
sum_=num1+num2
# debug(("addition of two no is {}").format(sum_))
debug((f"addition of two no is {sum_}"))
--------------------------------------------------------------------------------------------------------------------------
5)
 JSON file (javascript object notation)
:- it is mainly used for storing and transferring data between the browser and the server
json support :- array,string.number,object
:- it is data interchange format
:- it is a file in which data is written in text format

server side:-
* when sending data to client
 python to string
* when receiving data from client
 string to python

* dumps :- dic (python dictionary)to json string
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


import json
x=[1,2,3,4,5]
print(type(x))  list
y=json.dumps(x)
print(type(y))  str
--------------------------------------------------------------------------------------------------------------------------
6)
 pickling :- pickling refer to the process of converting the structure
               dic to byte before writing the file

import pickle
car=["audi", "bmw", "maruti"]
file="mycar.pkl"
fileobj=open(file,"wb")
pickle.dump(car,fileobj)
fileobj.close()

unpickling :- byte to original structure

for read
import pickle
file="mycar.pkl"
fileobj=open(file,"rb")
mycar=pickle.load(fileobj)
print(mycar)
---------------------------------------------------------------------------------------------------------------------------
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
---------------------------------------------------------------------------------------------------------------------------
12) multi threading
:- thread is a separate flow of execution. every thread has a task
:- Multithreading aims to perform multiple tasks simultaneously, which increases performance,
   speed and improves the rendering of the application.
:- when multiple processors are running on a program, each processor runs simultaneously to
   execute its tasks separately.
syntax:-
x=Thread(target=function_name,args=(arg1,arg2,..)

uses:-
1) multimedia graphic
2) animation
3) video games
4) web and application server

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

from threading import *
def show():
        for i in range(5):
            print("hii..")
t1=Thread(target=show)
t1.start()
for i in range(5):
    print("bye....")
-------------------------------------------------------------------------------------------------------------------------
13) enumerate :-

x=[10,20,30,40,50,60]
for i,j in enumerate(x):
    if i%2!=0:
        print(j)
o/p :-  20,40,60
------------------------------------------------------------------------------------------------------------------------
14) random
import random
# x=random.randint(1,99)
# print(x)

# x=[11,12,13,14]
# y=random.choice(x)
# print(y)
#
# x=[11,12,13,14]
# random.shuffle(x)
# print(x)

x=random.random()
print(x)
------------------------------------------------------------------------------------------------------------------------
15) datetime
from time import *
print(ctime())

#to find year
print(localtime().tm_mday,end='/')
print(localtime().tm_mon,end='/')
print(localtime().tm_year)

#
#
# print(localtime().tm_hour,end=':')
# print(localtime().tm_min,end=':')
# print(localtime().tm_sec)
-------------------------------------------------------------------------------------------------------------------------











'''