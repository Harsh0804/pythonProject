from tkinter import *
root=Tk()
r1=Radiobutton(root,text="YES",value=1)
r2=Radiobutton(root,text="NO",value=2)
r1.pack()
r2.pack()
root.geometry("300x300")
root.mainloop()