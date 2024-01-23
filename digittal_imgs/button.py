import tkinter as tk
from greyConver import GreyCon
from event import separate_EVENT,rote
def separete_but(x,y,window,path):
    canvas = tk.Canvas(window, width=100, height=30, bg="black")
    canvas.place(x=x,y=y)
    canvas.create_text(50, 15, text="separete", fill="white", font=("Arial", 12), anchor=tk.CENTER)
    canvas.bind("<Button-1>",lambda event, path=path,wd=window: separate_EVENT(event,path,wd))

def grey_convertBut(x,y,window,path):
    canvas =tk.Canvas(window,width=100,height=30, bg="black")
    canvas.place(x=x,y=y)
    canvas.create_text(50,15,text="ConvertGrey", fill="white", font=("Arial", 12), anchor=tk.CENTER)
    canvas.bind("<Button-1>",lambda event, path=path: GreyCon(event,path))

def Rotage(x,y,window,canvas,resized_image,image_item):
    canvas1 =tk.Canvas(window,width=100,height=30, bg="black")
    canvas1.place(x=x,y=y)
    canvas1.create_text(50,15,text="Rotage", fill="white", font=("Arial", 12), anchor=tk.CENTER)
    canvas1.bind("<Button-1>",lambda event,canvas=canvas,resized_image=resized_image,image_item=image_item: rote(event,canvas,resized_image,image_item))
    


        