from tkinter import *
from tkinter import messagebox

def mainwindow() :
   root = Tk()
   root.title("Week3-Lecture: Design layout using Frame by Nuttanon Rungpiton")
   root.geometry("600x500")
   root.configure(bg="lightgreen")
   root.rowconfigure(0, weight=1)
   root.rowconfigure(1, weight=4)
   root.columnconfigure(0, weight=1)
   root.columnconfigure(1, weight=4)
   return(root)

def createLayout(root) :
    top = Frame(root, bg="#404258")
    top.rowconfigure(0, weight=1)
    top.columnconfigure((0,1), weight=1)
    top.grid(row=0, column=0, columnspan=2, sticky="news")
    left = Frame(root, bg="#474E68")
    left.rowconfigure((0,1,2), weight=1)
    left.columnconfigure(0, weight=1)
    left.grid(row=1, column=0, sticky="news")
    right = Frame(root, bg="#50577A")
    right.rowconfigure((0,1,2), weight=1)
    right.columnconfigure(0, weight=1)
    right.grid(row=1, column=1, sticky="news")
    return(top, left, right)
    
def topWidget(top) :
    btn1 = Button(top, text="Click Me1", image=icon1, compound="top")
    btn1.grid(row=0, column=0, ipadx=30)
    btn2 = Button(top, text="Exit Program", image=icon2, compound="top", command=exitProgram)
    btn2.grid(row=0, column=1, ipadx=30)
    
def leftWidget(left) :
    label1 = Label(left, image=book1, bg="#474E68")
    label1.grid(row=0)
    label2 = Label(left, image=book2, bg="#474E68")
    label2.grid(row=1)
    label3 = Label(left, image=book3, bg="#474E68")
    label3.grid(row=2)
    
def rightWidget(right) :
    select1 = Button(right, text="Select book1", image=cartimg, compound="left", command=clickbook1)
    select1.grid(row=0, ipadx=30, ipady=10, sticky="w", padx=30)
    select2 = Button(right, text="Select book2", image=cartimg, compound="left", command=clickbook2)
    select2.grid(row=1, ipadx=30, ipady=10, sticky="w", padx=30)
    select3 = Button(right, text="Select book3", image=cartimg, compound="left", command=clickbook3)
    select3.grid(row=2, ipadx=30, ipady=10, sticky="w", padx=30)
    
def clickbook1() :
    messagebox.showinfo("Sirinthorn said: ","You select BOOK1")
def clickbook2() :
    messagebox.showinfo("Sirinthorn said: ","You select BOOK2")
def clickbook3() :
    messagebox.showinfo("Sirinthorn said: ","You select BOOK3")
def exitProgram() :
    answer = messagebox.askokcancel(title='Are you sure!', message='Exit the Program.')
    if answer:
        quit()

root = mainwindow()
icon1 = PhotoImage(file="image/icon1.png")
icon2 = PhotoImage(file="image/icon2.png")
book1 = PhotoImage(file="image/book1.png")
book2 = PhotoImage(file="image/book2.png")
book3 = PhotoImage(file="image/book3.png")
cartimg = PhotoImage(file="image/cart.png").subsample(2,2)
top, left, right = createLayout(root)
topWidget(top)
leftWidget(left)
rightWidget(right)
root.mainloop()