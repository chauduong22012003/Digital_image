from tkinter import Tk, Canvas, PhotoImage, Button
from PIL import Image, ImageTk



image_path = "HW1/scenary_imgs/anh1.png"

root = Tk()

canvas_width = 400
canvas_height = 400
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

image = Image.open(image_path)
resized_image = image.resize((50, 100))
# rotated_image = resized_image.rotate(45, expand=True)
# photo = ImageTk.PhotoImage(rotated_image)
rotated_image = resized_image.rotate(0, expand=True)
photo = ImageTk.PhotoImage(rotated_image)

image_item=canvas.create_image(canvas_width/2, canvas_height/2, image=photo)
canvas.image = photo


def A(canvas,resized_image,image_item):
    rotated_image = resized_image.rotate(90, expand=True)
    photo = ImageTk.PhotoImage(rotated_image)
    
    canvas.itemconfig(image_item, image=photo)
    canvas.image = photo
    





