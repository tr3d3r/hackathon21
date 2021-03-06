#this i calebs file
#need to use Tkinter (standard GUI lib)
#!/usr/bin/python
#tkinter should let us use buttons, labels, and text boxes


import tkinter as TKinter
import PIL as pillow
from tkinter import *
from PIL import ImageTK,Image
top = Tk()
canvas = Canvas(top, width = 300, height = 300)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("fooddrive.jpeg"))
canvas.create_image(20, 20, anchor=NW, image=img)


# import tkinter.messagebox

# top = tkinter.Tk()
# # Code to add things goes here
# # want to prompt user to add location or view current
# mb= Menubutton (top, text="Select One", relief=RAISED)
# mb.grid()
# mb.menu = Menu (mb, tearoff = 0)
# #tearoff accepts bool value to spear menu from main/parent window
# mb["menu"] = mb.menu

# addVar = IntVar()
# curVar = IntVar()

# #adding buttons
# mb.menu.add_checkbutton ( label="add a new location", variable=addVar )
# mb.menu.add_checkbutton ( label="view active locations", variable=curVar )

# mb.pack() #packs widgets in rows or columns

# # def menuCallBack():
# #     tkMesageBox.showifo( "Add Location", "Add New")

# # B = TKinter.Buttons(top, text ="Location", command = menuCallBack)

# # B.pack()
top.mainloop()