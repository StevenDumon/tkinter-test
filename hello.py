from tkinter import *

# Root widget, the window
root = Tk()

# Label widget in root widget
myLabel = Label(root, text = "Hello World")

# put it on the screen, pack in first available spot
myLabel.pack()

# Event loop, main loop of the program
root.mainloop()