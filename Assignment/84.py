# Python Program to Remove Punctuations From a String

y= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

x = "Hello!!!, he said ---and went."
z=""
for i in x:
    if i not in y:
        z = z + i
print(z)
