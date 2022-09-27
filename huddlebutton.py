from tkinter import *
from tkinter import messagebox

def call_me():
    messagebox.showinfo("Success","welcome to our tutorial")

root=Tk()
b=Button(root,text="Click here",command=call_me)
b.pack()
root.geometry("400x400")
root.mainloop()