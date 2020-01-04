#MESSAGE BOX
from tkinter import *
import tkinter.messagebox


root = Tk()

tkinter.messagebox.showinfo('Title','Swattik is a GOD.')

answer = tkinter.messagebox.askquestion('Question 1','Do you like AWP?')

if answer == 'yes':
    print(" DAMN NICE")


root.mainloop()