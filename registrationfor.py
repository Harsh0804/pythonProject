from tkinter import *
from tkinter import messagebox

window=Tk()
window.title(" Welcome to tutorial point")
window.geometry("400x400")
a=Label(window,text="First Name").grid(row=0,column=0)
b=Label(window,text="Last Name").grid(row=1,column=0)
c=Label(window,text="Email ID").grid(row=2,column=0)
d=Label(window,text="Contact Number").grid(row=3,column=0)
a1=Entry(window).grid(row=0,column=1)
b1=Entry(window).grid(row=1,column=1)
c1=Entry(window).grid(row=2,column=1)
d1=Entry(window).grid(row=3,column=1)

def call_me():
    messagebox.showinfo("Welcome","Successfully submitted")

b=Button(window,text="Click Here",command=call_me).grid(row=4,column=0)

window.mainloop()