list1=[12,56,32,45,89,12]
list2=[56,43,25,12,89,11]
list3=set(list1).intersection(set(list2))
def abc(x):
    if x:
      return True
    else:
        return False
result=list(filter(abc,list3))
print(result)

