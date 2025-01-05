from tkinter import *
from PIL import Image, ImageTk
import cv2

# Root widget, the main window
root = Tk()
root.geometry=("1200x700")
root.title("Webcam")

# Label widget to display image
label = Label(root)
label.frame_num=0
label.grid(row=0, column=0, rowspan=6)

# Define a video capture object
vid=cv2.VideoCapture(0)

# Declare the width and height in variables 
width, height = 800, 600
  
# Set the width and height 
vid.set(cv2.CAP_PROP_FRAME_WIDTH, width) 
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height) 

if not vid.isOpened():
    print("Cannot open camera")
    exit()

def show_frames():
    cv2image = cv2.cvtColor(vid.read()[1], cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    photo_image = ImageTk.PhotoImage(image=img)
    label.photo_image = photo_image
    # Configure image in the label
    label.configure(image=photo_image)
    # Repeat the same process after every 100 milliseconds
    label.after(50, show_frames)


# Button click actions
def button_inop_click():
    print("INOP btn clicked")

def button_blur_click():
    global status_blur
    # switch status and adjust btn color
    if status_blur==1:
        btn_blur.config(fg="black", bg="SystemButtonFace")
        status_blur = 0
    else:
        status_blur = 1
        btn_blur.config(fg="white", bg="green")


#def button_3_click(number):
    #e.insert(0,"number")

#def button_4_click(number):
#    e.insert(0,"number")

#def button_5_click(number):
#    e.insert(0,"number")

#def button_6_click(number):
#    e.insert(0,"number")

#def button_7_click(number):
#    e.insert(0,"number")

#def button_8_click(number):
#    e.insert(0,"number")


# buttons and their toggle status
global status_blur
status_blur= 0
btn_blur = Button(root, text="blur", padx=32, command=button_blur_click)
btn_blur.grid(row=0, column=1, columnspan=3)

#btn2 = Button(root, text="inop", padx=32, state=DISABLED, command=button_inop_click).grid(row=0, column=2)
#btn3 = Button(root, text="inop", padx=32, state=DISABLED, command=button_inop_click).grid(row=0, column=3)
#btn4 = Button(root, text="inop", padx=32, state=DISABLED, command=button_inop_click).grid(row=1, column=1)
#btn5 = Button(root, text="inop", padx=32, state=DISABLED, command=button_inop_click).grid(row=1, column=2)
#btn6 = Button(root, text="inop", padx=32, state=DISABLED, command=button_inop_click).grid(row=1, column=3)

# sliders
slider_1 = Scale(root, from_=100, to=0, orient=VERTICAL).grid(row=5, column=1)
slider_2 = Scale(root, from_=100, to=0, orient=VERTICAL).grid(row=5, column=2)
slider_3 = Scale(root, from_=100, to=0, orient=VERTICAL).grid(row=5, column=3)

# start the camera
show_frames()

# Event loop, main loop of the program
root.mainloop()