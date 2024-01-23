import tkinter as tk
from display import getMainFrame
from event import mouse_click_img1,mouse_click_img2,mouse_click_img3,mouse_click_img4,mouse_click_img5
from Separate  import separate
from button import separete_but,grey_convertBut,Rotage
import cv2 
from PIL import ImageTk, Image 

savepath="HW1/scenary_imgs/anh5.png"

goc=0
def mouse_click(event,i,canvas,image_item):
    
    print("Mouse clicked at ({}, {})".format(event.x, event.y))
    global goc
    
    path=""
    if i==0:
        path=mouse_click_img1(event)
    elif i==1:
        path=mouse_click_img2(event)
    elif i==2:
        path=mouse_click_img3(event)
    elif i==3:
        path=mouse_click_img4(event)
    elif i==4:
        path=mouse_click_img5(event)
    else:
        print("")
    # if(event.x)
    global savepath
    savepath=path
    image = cv2.imread(savepath)
    image = cv2.resize(image, (250, 350))
    image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    image_tk = ImageTk.PhotoImage(image_pil)
    # canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)
    canvas.itemconfig(image_item, image=image_tk)
    canvas.image = image_tk 
    separete_but(850,10,window,savepath)
    grey_convertBut(850,50,window,savepath)
    Rotage(850,90,window,canvas,image_pil,image_item)

# Create an instance of Tkinter
window = tk.Tk()

# Set the window title
window.title("Canvas List")

# Set the window size
window.geometry("1200x600")



canvas_list = []
mainFrame=getMainFrame(window)
mainFrame.place(x=300,y=10)

image_item = mainFrame.create_image(500/2, 500/2, image=None)


# Create a list of 5 Canvas objects
for i in range(5):
    canvas = tk.Canvas(window, width=70, height=70, bg="gray")
    canvas_list.append(canvas)
    image = cv2.imread("HW1/scenary_imgs/anh{}.png".format(i+1))
    resized_image = cv2.resize(image, (70, 70))
    resized_image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
    image_pil = Image.fromarray(resized_image_rgb)
    image_tk = ImageTk.PhotoImage(image_pil)
    canvas.create_image(0, 0, anchor="nw", image=image_tk)
    canvas.image = image_tk

# Set the position and display the Canvases on the window
for i, canvas in enumerate(canvas_list):
    
    
    canvas.bind("<Button-1>", lambda event, index=i,cv=mainFrame,image_item=image_item: mouse_click(event, index,cv,image_item))
    canvas.grid(row=i // 2, column=i % 2, padx=10, pady=10)


window.mainloop()





 
    


