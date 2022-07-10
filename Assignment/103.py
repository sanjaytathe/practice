# 2. You have a list of N+1 integers between 1 and N. You know there’s at least one duplicate,
# but there might be more. For example, if N=3, your list might be 3, 1, 1, 3 or it might be 1, 3, 2, 2
# Print out a number that appears in the list more than once.

x=[1,2,4,6,3,5,2,4,1,6]
y=[]
for i in x:
    if x.count(i)>1:
        y.append(i)
h=set(y)
print(list(h))