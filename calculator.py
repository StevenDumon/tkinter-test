from tkinter import *

# Root widget, the window
root = Tk()
root.title("Simple calculator")

#Enter number buttons
def button_click(number):
    e.insert(0,"number")

#entry inputbox on top
e = Entry(root, width=35).grid(row=0, column=0, columnspan=3)

# buttons, command mag geen parameters meesturen anders wordt die functie altijd onmiddellijk uitgevoerd
# Parameter meesturen met function mogelijk via "lambda"
btn7 = Button(root, text="7", padx=32, pady=16, command=lambda: button_click()).grid(row=1, column=0)
btn8 = Button(root, text="8", padx=32, pady=16, command=lambda: button_click()).grid(row=1, column=1)
btn9 = Button(root, text="9", padx=32, pady=16, command=lambda: button_click()).grid(row=1, column=2)
btn4 = Button(root, text="4", padx=32, pady=16, command=lambda: button_click()).grid(row=2, column=0)
btn5 = Button(root, text="5", padx=32, pady=16, command=lambda: button_click()).grid(row=2, column=1)
btn6 = Button(root, text="6", padx=32, pady=16, command=lambda: button_click()).grid(row=2, column=2)
btn1 = Button(root, text="1", padx=32, pady=16, command=lambda: button_click()).grid(row=3, column=0)
btn2 = Button(root, text="2", padx=32, pady=16, command=lambda: button_click()).grid(row=3, column=1)
btn3 = Button(root, text="3", padx=32, pady=16, command=lambda: button_click()).grid(row=3, column=2)
btn0 = Button(root, text="0", padx=32, pady=16, command=lambda: button_click()).grid(row=4, column=0)
btnClear = Button(root, text="Clr", padx=64, pady=16, command=lambda: button_click()).grid(row=4, column=1, columnspan=2)
btnPlus = Button(root, text="+", padx=31, pady=16).grid(row=5, column=0)
btnEquals = Button(root, text="=", padx=63, pady=16, command=lambda: button_click()).grid(row=5, column=1, columnspan=2)



# Event loop, main loop of the program
root.mainloop()