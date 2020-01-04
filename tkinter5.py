from tkinter import *

root = Tk()

canvas = Canvas(root,width=700, height=400)
canvas.pack()

blackline = canvas.create_line(0,0, 200,50)  #first 2 are start coordinates and 2nd two are end coordinates
redline = canvas.create_line(0,400, 200,50, fill="red")

greenBox = canvas.create_rectangle(25,25, 300,200,fill="green")



root.mainloop()