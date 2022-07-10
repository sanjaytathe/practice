from tkinter import *
from tkinter import ttk
#function coding
val=""
def press(num):
    global val
    val=val+str(num)
    var.set(val)
key=Tk()
#photo
key.iconbitmap("C:\\Users\\Asus\\Desktop\\calc.ico")
#title
key.title("keyboard by sanjay")
# window size
#key.geometry("1010x250")
key.minsize(width=1010,height=250)
key.maxsize(width=1010,height=250)
#enter box
var=StringVar()
display=Entry(key,state="readonly",textvariable=var,bg="red",bd=5)
display.pack()
display.grid(rowspan=1,columnspan=100,ipadx=999,ipady=20)
# background colour
key.configure(bg="yellow")
#button
#first line
q=Button(key,text="Q",command=lambda:press("Q"))
q.grid(row=1,column=0,ipadx=6,ipady=10)
w=Button(key,text="W",command=lambda:press("W"))
w.grid(row=1,column=1,ipadx=6,ipady=10)

def clear():
    global val
    val=" "
    var.set(val)
clear=Button(key,text="clear",width=6,command=clear)
clear.grid(row=1,column=39,ipadx=20,ipady=10)


#second line
a=Button(key,text="A",command=lambda:press("A"))
a.grid(row=2,column=0,ipadx=6,ipady=10)
s=Button(key,text="S",command=lambda:press("S"))
s.grid(row=2,column=1,ipadx=6,ipady=10)

def action():
    val="Next Line : "
    var.set(val)
enter=Button(key,text="Enter",width=6,command=action)
enter.grid(row=2,column=39,ipadx=6,ipady=15)


key.mainloop()