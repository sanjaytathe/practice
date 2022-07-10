#  Python program to check if a string is palindrome or not Reverse words in a given String in
s=input("enter the string :- ")
if s==s[::-1]:
    print("given string is palindrome")
else:
    print("given string is not palindrome")