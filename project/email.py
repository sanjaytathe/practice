email=input(" enter your  email")
a,b,c=0,0,0
if len(email)>6:
    if email[0].isalpha():
        if ('@' in email) and (email.count('@')==1):
            if (email[-3]=='.') ^ (email[-4]=='.'):
                for i in email:
                    if i==i.isspace():
                        a=1
                    elif i.isalpha():
                        if i==i.upper():
                         b=1
                    elif i==i.isdigit():
                        continue
                    elif i=='@' or i=='.':
                        continue
                    else:
                        c=1
                if a==1 or b==1 or c==1:
                    print(" wrong email 5")
                else:
                    print(" right email")

            else:
               print(" wrong email 4")
        else:
           print(" wrong email 3")
    else:
        print(" wrong email 2")
else:
    print(" wrong email 1")
