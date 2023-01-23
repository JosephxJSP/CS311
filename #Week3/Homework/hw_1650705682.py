from tkinter import *
from tkinter import messagebox

def mainWindow() :
    root = Tk()
    root.title("")
    root.geometry("600x500")
    root.configure(bg="lightgreen")
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=4)
    root.rowconfigure(2, weight=3)
    root.columnconfigure(0, weight=6)
    root.columnconfigure(1, weight=2)
    return(root)

def createLayout(root) :
    top = Frame(root, bg="#404258")
    top.rowconfigure(0, weight=1)
    top.columnconfigure(0, weight=1)
    top.grid(row=0, column=0, columnspan=2, sticky="news")
    
    mid = Frame(root, bg="#404258")
    
    return(top)
    
root = mainWindow()
top = createLayout(root)
root.mainloop(0)