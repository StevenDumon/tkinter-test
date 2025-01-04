from tkinter import *

# Root widget, the window
root = Tk()

# Label widget in root widget
myLabel1 = Label(root, text = "Hello World")
myLabel2 = Label(root, text = "Label 2 text in grid")
myLabel3 = Label(root, text = ".")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=1, column=1)

# Event loop, main loop of the program
root.mainloop()