from tkinter import *

root = Tk()
root.geometry("1000x1000")
root.title("VS paint")

paint = Button(root,text="Paint",padx=3,pady=3)
brush = Button(root,text="Brush",padx=3,pady=3)
rubber = Button(root,text="Rubber",padx=3,pady=3)
colour = Button(root,text="Colour",padx=3,pady=3)
cans = Canvas(root,bg="White",width=1500,height=1500)
scroll = Scale(root,bg="grey",width=50,from_=1,to=2,orient="horizontal")

scroll.grid(row=0,column=5)
cans.grid(row=2,column=0,columnspan=5)
paint.grid(row=0,column=1)
brush.grid(row=0,column=2)
rubber.grid(row=0,column=3)
colour.grid(row=0,column=4)

root.mainloop()