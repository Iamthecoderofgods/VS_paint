from tkinter import *
from tkinter import colorchooser



root = Tk()
root.geometry("1000x1000")
root.title("VS paint")

oldX= None
oldy= None


size = 0
tool = ""
brushcolour = "Black"



paint = Button(root,text="Paint",padx=3,pady=3)
brush = Button(root,text="Brush",padx=3,pady=3)
rubber = Button(root,text="Rubber",padx=3,pady=3)
colour = Button(root,text="Colour",padx=3,pady=3)
cans = Canvas(root,bg="White",width=880,height=1000)

scroll = Scale(root,bg="grey",width=50,from_=1,to=10,orient="horizontal")
size = scroll.get()
scroll.set(5)
def paint_button(event):
    global oldX, oldy, brushcolour
    size = scroll.get()
    x1 = event.x - size
    y1 = event.y - size
    x2 = event.x + size
    y2 = event.y + size
    if tool == "Pen" or "Brush":
        cans.create_line(x1,y1,x2,y2,fill=brushcolour,width=size,smooth=True,capstyle=ROUND)
    elif tool == "Rubber":
        brushcolour = "white"
        cans.create_line(x1,y1,x2,y2,fill=brushcolour,width=size,smooth=True,capstyle=ROUND)
    oldX = event.x
    oldy = event.y
def startpaint(event):
    global oldX, oldy
    oldX = event.x
    oldy = event.y
def pens():
    global tool, brushcolour
    tool = "Pen"
    brushcolour = "black"
def Use_Rubber():
    global tool, brushcolour
    tool = "Rubber"
    brushcolour = "white"
def brush_button():
    global tool, brushcolour
    tool = "Brush"
    brushcolour = "black"
def colour_picker():
    global brushcolour
    brushcolour = colorchooser.askcolor(color=brushcolour)[1]
    
    

cans.bind("<B1-Motion>",paint_button)
cans.bind("<Button-1>",startpaint)

rubber.config(command=Use_Rubber)
paint.config(command=pens)
brush.config(command=brush_button)
colour.config(command=colour_picker)
scroll.grid(row=0,column=5)
cans.grid(row=2,column=0,columnspan=5)
paint.grid(row=0,column=1)
brush.grid(row=0,column=2)
rubber.grid(row=0,column=3)
colour.grid(row=0,column=4)

root.mainloop()