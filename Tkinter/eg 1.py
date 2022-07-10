# from tkinter import *
# root=Tk()
# root.title("my first claculator")
# label=Label(root,font=("Ariel",16),text="enter your name",bg="red",fg="pink")
# label.pack()
# root.geometry("400x500+300+150")
# root.resizable(0,0)
# root.mainloop()



#
# from tkinter import *
# root=Tk()
# root.title("my first claculator")
# root.geometry("400x500+300+150")
# display=Entry(root,font=("Ariel",16),bd=29,bg="red",justify="right",fg="pink")
#
# display.grid(row=0,columnspan=2)
# # root.geometry("400x500+300+150")
# #root.resizable(0,0)
# root.mainloop()



from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root=Tk()
root.title("my first claculator")
root.maxsize(width=600,height=300)
root.minsize(width=600,height=300)
#function
# def func():
#     x=var.get()
#     lbl.config(text=x)
# #label
# lbl=Label(root,text="user name",bg="red",fg="white")
# lbl.place(x=10,y=10)

# lbl=Label(root,text="nothing",bg="red",fg="white")
# lbl.place(x=40,y=100)
# #entry
# var=StringVar()
# ent=Entry(root,bg="red",fg="white",bd=15,textvariable=var)
# ent.place(x=80,y=10)
#
# #button
# btn=Button(root,text="submit",bg="green",command=func)
# btn.place(x=10,y=50)

#combobox
# var=StringVar()
# com=ttk.Combobox(root,width=50,textvariable=var)
# com['state']='randomnly'
# com['values']=('jan','feb')
# com.current(0)
# com.place(x=10,y=10)
#



# #checkbutton
# def func():
#     print(Checkbtn1.get())
#     print(Checkbtn2.get())
# Checkbtn1=IntVar()
# Checkbtn2=IntVar()
#
# select=Checkbutton(root,text="male",variable=Checkbtn1,onvalue=1,offvalue=0)
# select.pack()
# select=Checkbutton(root,text="female",variable=Checkbtn2,onvalue=1,offvalue=0)
# select.pack()
# btn=Button(root,text="data get",command=func).pack()


# def func():
#     if var.get()==0:
#         print("male")
#     else:
#         print("female")
# var=IntVar()
# radio1=Radiobutton(root,text="male",value=0,variable=var).pack()
# radio2=Radiobutton(root,text="female",value=1,variable=var).pack()
#
# btn=Button(root,text="submit",command=func).pack()
# root.mainloop()


# FRAME
# bottom=Frame(root)
# bottom.pack(side=BOTTOM)
# label=Label(bottom,text="this is bottom")
# label.pack(side=BOTTOM)



#message
# def func():
#     if var.get()=="":
#         messagebox.showwarning("warning","empty box")
#     else:
#         messagebox.showinfo("success",var.get())
# var=StringVar()
# ent=Entry(root,textvariable=var)
# ent.pack()
# btn=Button(root,text="click me",command=func)
# btn.pack()
# root.mainloop()


#listbox
lst=Listbox(root,width=27)
items=["apple","banana"]
for i in items:
    lst.insert(END,i)
lst.pack()
root.mainloop()



















