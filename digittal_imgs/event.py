import tkinter as tk
import cv2
from PIL import ImageTk, Image
from Separate import separate

# def mouse_click(event,i,canvas):
#     print("Mouse clicked at ({}, {})".format(event.x, event.y))
#     global path
#     if i==0:
#         path=mouse_click_img1(event)
#     elif i==1:
#         path=mouse_click_img2(event)
#     elif i==2:
#         path=mouse_click_img3(event)
#     elif i==3:
#         path=mouse_click_img4(event)
#     elif i==4:
#         path=mouse_click_img5(event)
#     else:
#         print("")
#     # if(event.x)
   
#     image = cv2.imread(path)
#     image = cv2.resize(image, (300, 500))
#     image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
#     image_tk = ImageTk.PhotoImage(image_pil)
#     canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)
#     canvas.image = image_tk  
    



def mouse_click_img1(event):
    print("Mouse clicked at 1")
    return "HW1/scenary_imgs/anh1.png"

def mouse_click_img2(event):
    print("Mouse clicked at 2")
    return "HW1/scenary_imgs/anh2.png"
def mouse_click_img3(event):
    print("Mouse clicked at 3")
    return "HW1/scenary_imgs/anh3.png"

def mouse_click_img4(event):
    print("Mouse clicked at img 4")
    return "HW1/scenary_imgs/anh4.png"

def mouse_click_img5(event):
    print("Mouse clicked at img5")
    return "HW1/scenary_imgs/anh5.png"


def separate_EVENT(event,path,window):
   
    separate(path,window)
goc=0
def rote(event,canvas,resized_image,image_item):
    global goc
    goc=goc+45
    rotated_image = resized_image.rotate(goc, expand=True)
    photo = ImageTk.PhotoImage(rotated_image)
    
    canvas.itemconfig(image_item, image=photo)
    canvas.image = photo
    