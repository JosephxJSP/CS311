from tkinter import *
from tkinter import messagebox

def mainWindow() :
    root = Tk()
    root.title("")
    root.geometry("1000x600")
    root.configure(bg="lightgreen")
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=6)
    root.rowconfigure(2, weight=1)
    root.columnconfigure(0, weight=1)
    root.title("GUI3: Class Activity of Week4 created by Nuttanon Rungpiron")
    icon = PhotoImage(file="image/icon2.png")
    root.iconphoto(False, icon)
    return(root)


def createLayout(root) :
    top = Frame(root, bg="#404258")
    top.rowconfigure(0, weight=1)
    top.columnconfigure(0, weight=1)
    top.grid(row=0, column=0, sticky="news")
    
    mid = Frame(root, bg="#EAC7C7")
    mid.rowconfigure(0, weight=1)
    mid.rowconfigure(1, weight=1)
    mid.rowconfigure(2, weight=1)
    mid.columnconfigure(0, weight=1)
    mid.columnconfigure(1, weight=1)
    mid.columnconfigure(2, weight=2)
    mid.grid(row=1, column=0, sticky="news")

    bottom = Frame(root, bg="#50577A")
    bottom.rowconfigure(0, weight=1)
    bottom.columnconfigure(0, weight=1)
    bottom.grid(row=2, column=0, sticky="news")

    return(top, mid, bottom)


def addTopWidget(top) :
    title = Label(top, text="My Cake Shop by Nuttanon", bg="#404258", fg="#8C91C0", font=("Leelawadee bold", 18))
    title.grid(row=0, column=0)


def addMidWidget(mid) :
    cake1 = Label(mid, bg="#EAC7C7", image=img_cake1).grid(row=0, column=0, sticky="news")
    cake2 = Label(mid, bg="#EAC7C7", image=img_cake2).grid(row=1, column=0, sticky="news")
    cake3 = Label(mid, bg="#EAC7C7", image=img_cake3).grid(row=2, column=0, sticky="news")

    frame_info1 = Frame(mid, bg="#EAC7C7")
    frame_info1.rowconfigure((0,1), weight=1)
    frame_info1.columnconfigure(0, weight=1)
    frame_info1.grid(row=0, column=1, sticky="news")
    frame_info2 = Frame(mid, bg="#EAC7C7")
    frame_info2.rowconfigure((0,1), weight=1)
    frame_info2.columnconfigure(0, weight=1)
    frame_info2.grid(row=1, column=1, sticky="news")
    frame_info3 = Frame(mid, bg="#EAC7C7")
    frame_info3.rowconfigure((0,1), weight=1)
    frame_info3.columnconfigure(0, weight=1)
    frame_info3.grid(row=2, column=1, sticky="news")
    Label(frame_info1, text="Chocolate Cake\nPrice 160 baths", bg="#EAC7C7", fg="#000000", font=("Leelawadee bold", 12)).grid(row=0, column=0, sticky="s")
    input1 = Spinbox(frame_info1, width=35, justify="center", from_=0, to=100)
    input1.grid(row=1, column=0, ipady=3)
    Label(frame_info2, text="Strawberry Cake\nPrice 170 baths", bg="#EAC7C7", fg="#000000", font=("Leelawadee bold", 12)).grid(row=0, column=0, sticky="s")
    input2 = Spinbox(frame_info2, width=35, justify="center", from_=0, to=100)
    input2.grid(row=1, column=0, ipady=3)
    Label(frame_info3, text="Donut Party\nPrice 45 baths", bg="#EAC7C7", fg="#000000", font=("Leelawadee bold", 12)).grid(row=0, column=0, sticky="s")
    input3 = Spinbox(frame_info3, width=35, justify="center", from_=0, to=100)
    input3.grid(row=1, column=0, ipady=3)

    msg1 = Label(mid, text="Thank You for your shopping\nTotal Price is", bg="#EAC7C7", fg="#000000", font=("Leelawadee bold", 18))
    msg1.grid(row=0, column=2)
    msg2 = Label(mid, text="0 Bath", bg="#EAC7C7", fg="blue", font=("Leelawadee bold", 18))
    msg2.grid(row=1, column=2)

    return msg2, input1, input2, input3


def addBottomWidget(bottom) :
    btn1 = Button(bottom, text="Exit Program", command=exitProgram)
    btn1.grid(column=0, row=0, ipadx=40, ipady=20, padx=20, sticky="e")
    

def exitProgram() :
    answer = messagebox.askokcancel(title="Are you sure!", message="Exit the Program.", icon="warning")
    if answer:
        quit()


def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def get_spinbox_value(*args):
    value1 = input1.get()
    value2 = input2.get()
    value3 = input3.get()

    if not is_valid_number(value1) or not is_valid_number(value2) or not is_valid_number(value3):
        msg2.config(text="กรุณากรอกจำนวนเป็นตัวเลขเท่านั้น")
    else:
        summary = (int(value1) * 160) + (int(value2) * 170) + (int(value3) * 45)
        msg2.config(text="%s Bath"%summary)



root = mainWindow()
top, mid, bottom = createLayout(root)
img_cake1 = PhotoImage(file="image/cake1.png")
img_cake2 = PhotoImage(file="image/cake2.png")
img_cake3 = PhotoImage(file="image/cake3.png")
addTopWidget(top)
msg2, input1, input2, input3 = addMidWidget(mid)
input1.bind("<FocusOut>", get_spinbox_value)
input2.bind("<FocusOut>", get_spinbox_value)
input3.bind("<FocusOut>", get_spinbox_value)
addBottomWidget(bottom)
root.mainloop(0)