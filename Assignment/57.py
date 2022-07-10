def deletion(str):
    string_=str
    substring=input("enter the substring: ")
    str2=str.find(substring)
    if str2!=-1:
        str=str.replace(substring,"")
        if str==substring:
            print('yes substring can delete the whole string')
        else:
            print("cannot delete "+string_+' using '+substring)
    elif str2==-1:
        print("cannot delete "+string_+' using '+substring)
str=input("enter the string: ")
deletion(str)