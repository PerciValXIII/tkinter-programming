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

#******CREATING A TOOL BAR******

toolbar = Frame(root,bg="blue")

insertButt = Button(toolbar, text="Insert Image",bg="green",command =doNothing)
insertButt.pack(side=LEFT, padx=2,pady=2)
printButt = Button(toolbar, text="Print",command=doNothing)
printButt.pack(side=LEFT,padx=2,pady=2)

toolbar.pack(side=TOP,fill=X)


#******CREATING A STATUS BAR******
status = Label(root,text="Preparing to do Nothing...",bd=1,relief=SUNKEN, anchor =W)
status.pack(side=BOTTOM, fill=X)


root.mainloop()