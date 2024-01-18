import cv2
import tkinter as tk
from PIL import Image, ImageTk

def display_image(image1,image2,image3,window):

    window1 = tk.Toplevel(window)
    window1.title()
    window1.geometry("1000x600")

    # canvas_width = image.shape[1]
    # canvas_height = image.shape[0]
    canvas1 = tk.Canvas(window1, width=300, height=500)
    resized_image1 = cv2.resize(image1, (300, 500))
    image_pil1 = Image.fromarray(resized_image1)
    image_tk1 = ImageTk.PhotoImage(image_pil1)
    canvas1.create_image(0, 0, anchor=tk.NW, image=image_tk1)

    canvas2 = tk.Canvas(window1, width=300, height=500)
    resized_image2 = cv2.resize(image2, (300, 500))
    image_pil2 = Image.fromarray(resized_image2)
    image_tk2 = ImageTk.PhotoImage(image_pil2)
    canvas2.create_image(0, 0, anchor=tk.NW, image=image_tk2)

    canvas3 = tk.Canvas(window1, width=300, height=500)
    resized_image3 = cv2.resize(image3, (300, 500))
    image_pil3 = Image.fromarray(resized_image3)
    image_tk3 = ImageTk.PhotoImage(image_pil3)
    canvas3.create_image(0, 0, anchor=tk.NW, image=image_tk3)
    
    canvas1.place(x=10, y=10)
    canvas2.place(x=320, y=10)
    canvas3.place(x=630, y=10)

    window1.mainloop()
def separate(path,window):

    image_path = path


    image = cv2.imread(image_path)


    b, g, r = cv2.split(image)


    display_image(r,g,b,window)
    # display_image(g, "Green Channel",window)
    # display_image(b, "Blue Channel",window)


