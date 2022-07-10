course = {
    'python': {'duration': '2 month', 'fees': 8000},
    'java': {'duration': '4 month', 'fees': 10000},
    'c++': {'duration': '3 month', 'fees': 6000},
}
opr = int(input('''
 do yo want to update any data
 1 yes
 2 no'''))
if opr==1:
    a = int(input('''
       what you want to update
       1 duration
       2 fees'''))
    subject = int(input('''
     please select subject
     1 python
     2 java
     3 c++'''))
    if opr == 1:
        if a == 1:
            if subject == 1:
                a = int(input("enter month"))
                course['python']['duration'] = a, 'month'
                for c, d in course.items():
                    print(c, d)
            elif subject == 2:
                a = int(input("enter month"))
                course['java']['duration'] = a, 'month'
                for c, d in course.items():
                    print(c, d)
            elif subject == 3:
                a = int(input("enter month"))
                course['c++']['duration'] = a, 'month'
                for c, d in course.items():
                    print(c, d)
        if a == 2:
            if subject == 1:
                a = int(input("enter fees"))
                course['python']['fees'] = a
                for c, d in course.items():
                    print(c, d)
            if subject == 2:
                a = int(input("enter fees"))
                course['java']['fees'] = a
                for c, d in course.items():
                    print(c, d)
            if subject == 3:
                a = int(input("enter fees"))
                course['c++']['fees'] = a
                for c, d in course.items():
                    print(c, d)
if opr == 2:
        print("thank  you")