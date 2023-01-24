from tkinter import *
from tkinter import messagebox
from tkinter import ttk

config = {}
config["sex"] = "M"                         # f=ผู้หญิง || m=ผู้ชาย || ไม่ใส่หรือใส่ค่าอื่นๆ=ไม่ระบุ
config["name"] = "Nuttanon Rungpiron"
config["position"] = "Student"
config["group"] = "Information Technology and Innovation"
# Infomation
config["age"] = 19
config["weight"] = 78
config["height"] = 183
config["skill"] = 5


def mainWindow() :
    root = Tk()
    root.title("")
    root.geometry("1000x600")
    root.configure(bg="lightgreen")
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=2)
    root.rowconfigure(2, weight=1)
    root.columnconfigure((0,1,2,3), weight=6)
    root.title("Dashboard by " + config["name"])
    icon = PhotoImage(file="images/icon2.png")
    root.iconphoto(False, icon)
    return(root)


def createLayout(root) :
    top = Frame(root, bg="#404258")
    top.rowconfigure(0, weight=1)
    top.columnconfigure(0, weight=1)
    top.grid(row=0, column=0, columnspan=4, sticky="news")
    
    mid = Frame(root, bg="#EAC7C7")
    mid.rowconfigure(0, weight=8)
    mid.columnconfigure(0, weight=4)
    mid.columnconfigure(1, weight=1)
    mid.grid(row=1, column=0, columnspan=4, sticky="news")

    bottom = Frame(root, bg="#50577A")
    bottom.rowconfigure(0, weight=3)
    bottom.columnconfigure((0,1,2,3), weight=2)
    bottom.grid(row=2, column=0, columnspan=4, sticky="news")

    return(top, mid, bottom)


def addTopWidget(top) :
    title = Label(top, text="Dashboard by " + config["name"], bg="#404258", fg="#8C91C0", font=("Leelawadee bold", 18))
    title.grid(row=0, column=0)


def addMidFrame(mid) :
    mid_l = Frame(mid, bg="#474E68")
    mid_l.rowconfigure(0, weight=3)
    mid_l.rowconfigure(1, weight=1)
    mid_l.columnconfigure((0,1,2,3), weight=2)
    mid_l.grid(row=0, column=0, sticky="news")
    mid_r = Frame(mid, bg="#FFFFFF")
    mid_r.rowconfigure(0, weight=1)
    mid_r.rowconfigure(1, weight=2)
    mid_r.columnconfigure(0, weight=1)
    mid_r.grid(row=0, column=1, sticky="news")
    return(mid_l, mid_r)


def addMidLeftWidget(mid_l) :
    profile_img = Label(mid_l, bg="#474E68", image=profile)
    profile_img.grid(row=0, column=0, sticky="news")
    profile_info = Label(mid_l, bg="#474E68", fg="#DEDEDE", font=("Leelawadee", 18), text="Mr."+config["name"]+"\n"+config["position"]+"\n"+config["group"]+"")
    profile_info.grid(row=0, column=1, columnspan=3, sticky="w", ipadx=20)

    age_frame = Frame(mid_l, bg="#53A551")
    age_frame.rowconfigure((0,1), weight=1)
    age_frame.columnconfigure(0, weight=5)
    age_frame.grid(row=1, column=0, sticky="news")
    Label(age_frame, text=config["age"], bg="#53A551", fg="#FFFFFF", font=("Leelawadee bold", 24)).grid(row=0)
    Label(age_frame, text="Age", bg="#53A551", fg="#FFFFFF", font=("Leelawadee", 14)).grid(row=1, sticky="n")

    weight_frame = Frame(mid_l, bg="#F5C344")
    weight_frame.rowconfigure((0,1), weight=1)
    weight_frame.columnconfigure(0, weight=5)
    weight_frame.grid(row=1, column=1, sticky="news")
    Label(weight_frame, text=config["weight"], bg="#F5C344", fg="#FFFFFF", font=("Leelawadee bold", 24)).grid(row=0)
    Label(weight_frame, text="Weight", bg="#F5C344", fg="#FFFFFF", font=("Leelawadee", 14)).grid(row=1, sticky="n")

    height_frame = Frame(mid_l, bg="#4BA0B5")
    height_frame.rowconfigure((0,1), weight=1)
    height_frame.columnconfigure(0, weight=5)
    height_frame.grid(row=1, column=2, sticky="news")
    Label(height_frame, text=config["height"], bg="#4BA0B5", fg="#FFFFFF", font=("Leelawadee bold", 24)).grid(row=0)
    Label(height_frame, text="Height", bg="#4BA0B5", fg="#FFFFFF", font=("Leelawadee", 14)).grid(row=1, sticky="n")

    skill_frame = Frame(mid_l, bg="#CB444A")
    skill_frame.rowconfigure((0,1), weight=1)
    skill_frame.columnconfigure(0, weight=5)
    skill_frame.grid(row=1, column=3, sticky="news")
    Label(skill_frame, text=config["skill"], bg="#CB444A", fg="#FFFFFF", font=("Leelawadee bold", 24)).grid(row=0)
    Label(skill_frame, text="Skill", bg="#CB444A", fg="#FFFFFF", font=("Leelawadee", 14)).grid(row=1, sticky="n")


def addMidRightWidget(mid_r) :
    label1 = Label(mid_r, bg="#FFFFFF", font=("Leelawadee bold", 18), fg="#404258", text="My English Skill")
    label1.grid(row=0, column=0, sticky="ws", ipadx=20)
    label1 = Label(mid_r, bg="#FFFFFF", image=skill_img)
    label1.grid(row=1, column=0)

    
def addBottomWidget(bottom) :
    btn1 = Button(bottom, text="Click me 1", command=lambda:showInfoModal("Click me 1 clicked"))
    btn1.grid(column=0, row=0, ipadx=30, ipady=10)
    btn2 = Button(bottom, text="Click me 2", command=lambda:showInfoModal("Click me 2 clicked"))
    btn2.grid(column=1, row=0, ipadx=30, ipady=10)
    btn3 = Button(bottom, text="Click me 3", command=lambda:showInfoModal("Click me 3 clicked"))
    btn3.grid(column=2, row=0, ipadx=30, ipady=10)
    btn4 = Button(bottom, text="Exit Program", command=exitProgram)
    btn4.grid(column=3, row=0, ipadx=30, ipady=10)


def showInfoModal(msg) :
    messagebox.showinfo("Nuttanon said:", msg)


def exitProgram() :
    answer = messagebox.askokcancel(title="Are you sure!", message="Exit the Program.", icon="warning")
    if answer:
        quit()


def checkSex() :
    if config["sex"].lower() == "f" :
        return(PhotoImage(file="images/female.png").subsample(3,3))
    elif config["sex"].lower() == "m" :
        return(PhotoImage(file="images/male.png").subsample(3,3))
    else:
        return(PhotoImage(file="images/agender.png").subsample(3,3))
    
root = mainWindow()
top, mid, bottom = createLayout(root)
mid_l, mid_r = addMidFrame(mid)
profile = checkSex()
skill_img = PhotoImage(file="images/skill.png")
addTopWidget(top)
addMidLeftWidget(mid_l)
addMidRightWidget(mid_r)
addBottomWidget(bottom)
root.mainloop(0)