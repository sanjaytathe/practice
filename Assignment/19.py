# Count occurrences of an element in a list

x=[1,5,9,8,5,6,7,5,4,6]
y=int(input("which no you want to check"))
count=0
for i in x:
    if (i==y):
        count=count+1
print(count)


y=[int(x) for x in input("enter the element").split(',')]
ele=int(input("enter the element"))
index=0
while index<len(y):
    if y[index]==ele:
        print(index,end=" ")
    index=index+1