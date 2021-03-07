#this i calebs file
#need to use Tkinter (standard GUI lib)
#!/usr/bin/python
#tkinter should let us use buttons, labels, and text boxes


# # import image
# from tkinter import *
# from PIL import ImageTk,Image
# top = Tk()
# canvas = Canvas(top, width = 300, height = 3000000, bg='black')
# canvas.pack()
# img = ImageTk.PhotoImage(Image.open("assets/fooddrive.jpg"))
# canvas.create_image(20, 20, anchor=NW, image=img)
import tkinter as TKinter
from tkinter import *
import tkinter.messagebox as tkMessageBox

top = TKinter.Tk()
top.title('Hackathon 2021')
top.geometry('300x100')

class Window(TKinter.Tk):
    """ Main class """
    def printSomething():
        button.destroy()
        label = Label(top, text= "GREETINGS")
        label.pack
    
    def menuCallBack():
        tkMessageBox.showinfo("Add location", "Add New")
    def menuCallAgain():
        tkMessageBox.showinfo("View Current", "View")

B = TKinter.Button(top, text ="Location", command = Window.menuCallBack)
C = TKinter.Button(top, text ="Current", command = Window.menuCallAgain)
button = Button(top, text="Print Me", command= Window.printSomething)

B.pack()
C.pack()
button.pack


top.mainloop()

# Code to add things goes here
# want to prompt user to add location or view current
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
 
#  def menuCallBack():
#      tkMesageBox.showifo( "Add Location", "Add New")
 
# B = TKinter.Buttons(top, text ="Location", command = menuCallBack)
 
#  B.pack()
 
#closes window
# import tkinter as tk
 
# class Test():
#     def __init__(self):
#         self.top = tk.Tk() 
#         self.top.geometry('100x50')
#         button = tk.Button(self.top,
#                             text = 'Click and Quit',
#                             command=self.quit)
#         button.pack()
#         self.top.mainloop()
 
#     def quit(self):
#         self.top.destroy()
# app = Test()
# # top.mainloop()
