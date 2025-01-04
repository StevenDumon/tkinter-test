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
label.grid(row=0, column=0, rowspan=3)

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
    # Repeat the same process after every 10 seconds
    label.after(10, show_frames)

def take_pic():
    file_name = f"{label.frame_num}.png"
    imagetk = label.imgtk
    imgpil = ImageTk.getimage(imagetk)
    imgpil.save(file_name, "PNG")
    imgpil.close()

# Button click actions
def button_1_click():
    take_pic()

#def button_2_click(number):
    #e.insert(0,"number")

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


# buttons
btn1 = Button(root, text="grab", padx=32, command=button_1_click).grid(row=0, column=1)
btn2 = Button(root, text="inop", padx=32, state=DISABLED, command=button_1_click).grid(row=0, column=2)
btn3 = Button(root, text="inop", padx=32, state=DISABLED, command=button_1_click).grid(row=0, column=3)
btn4 = Button(root, text="inop", padx=32, state=DISABLED, command=button_1_click).grid(row=1, column=1)
btn5 = Button(root, text="inop", padx=32, state=DISABLED, command=button_1_click).grid(row=1, column=2)
btn6 = Button(root, text="inop", padx=32, state=DISABLED, command=button_1_click).grid(row=1, column=3)

# sliders
slider_1 = Scale(root, from_=0, to=100, orient=VERTICAL).grid(row=2, column=1)
slider_2 = Scale(root, from_=0, to=100, orient=VERTICAL).grid(row=2, column=2)
slider_3 = Scale(root, from_=0, to=100, orient=VERTICAL).grid(row=2, column=3)

# start the camera
show_frames()

# Event loop, main loop of the program
root.mainloop()