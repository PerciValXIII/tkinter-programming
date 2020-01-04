#Creating drop down menus
from tkinter import *


def doNothing():
    print("OK OK I WONT")

root = Tk()

main_menu = Menu(root)
root.config(menu=main_menu)

subMenu = Menu(main_menu)
main_menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New Project",command= doNothing)
subMenu.add_command(label="New",command= doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit",command = doNothing)

editMenu=Menu(main_menu)
main_menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="redo",command=doNothing)


root.mainloop()