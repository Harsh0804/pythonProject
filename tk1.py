import tkinter
top=tkinter.Tk()
Can=tkinter.Canvas(top,bg="red",height=300,width=300)
coord=100,200,200,300
arc=Can.create_arc(coord,start=0,extent=270,fill="grey")
Can.create_rectangle(10,10,110,110,outline="black",fill="white",width=2)
Can.pack()
top.mainloop()