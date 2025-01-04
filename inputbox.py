from tkinter import *

# Root widget, the window
root = Tk()


# get the button do do something with function
def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()

# inputbox = entry widget
e = Entry(root, width=50)
e.pack()
# default value at index 0
e.insert(0, "default")

myButton = Button(root, text="Enter name", command=myClick)
myButton.pack()

# Event loop, main loop of the program
root.mainloop()