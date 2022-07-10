'''
string and dictionary
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

11.format()
----------------------------
4)Dictionary
* dictionary is unordered collection of key-value pair
* dic is used to
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

# x={x:x*x for x in range(10) if x%2==0}
# print(x)
#
# x={x:x*x for x in range(10) }
# print(x)


x = dict([(1,'apple'), (2,'ball')])
print(x)









'''