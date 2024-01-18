import tkinter as tk

from event import separate_EVENT
def separete_but(x,y,window,path):
    canvas = tk.Canvas(window, width=100, height=30, bg="black")
    canvas.place(x=x,y=y)
    canvas.create_text(50, 15, text="separete", fill="white", font=("Arial", 12), anchor=tk.CENTER)
    canvas.bind("<Button-1>",lambda event, path=path,wd=window: separate_EVENT(event,path,wd))
        