from tkinter import *

# Root widget, the window
root = Tk()


# get the button do do something with function
def myClick():
    myLabel = Label(root, text="Button is clicked.")
    myLabel.pack()
    myButton.config(bg="green")

# myButton = Button(root, text="Click me", state=DISABLED)
# change size, wider
#myButton = Button(root, text="Click me", padx=50)
# assign command, zonder haakjes, ander wordt die code al onmiddellijk uitgevoerd
myButton = Button(root, text="Click me", command=myClick)
myButton.pack()


# Event loop, main loop of the program
root.mainloop()