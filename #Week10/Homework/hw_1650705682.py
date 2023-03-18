from tkinter import *
from tkinter import messagebox
import sqlite3

def mainWindow() :
    root = Tk()
    w = 1000
    h = 600
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d" %(w,h,x,y))
    root.config(bg="#E9A178")
    root.title("Grade Report by Nuttanon Rungpiron")
    root.option_add("*font", "Garamond 24 bold")
    root.rowconfigure((0,1,2,3), weight=1)
    root.columnconfigure((0,1,2,3), weight=1)
    return(root)

def loginpage(root) : 
    global userentry, pwdentry, loginframe

    loginframe = Frame(root, bg="#F6E1C3")
    loginframe.rowconfigure((0,1,2,3), weight=1)
    loginframe.columnconfigure((0,1), weight=1)

    Label(loginframe, text="Login to view your grade", font="Garamond 26 bold", fg="blue", image=pic, compound=LEFT, bg="#F6E1C3").grid(row=0, columnspan=2)
    Label(loginframe, text="Username : ", bg="#F6E1C3", fg="#4a3933", padx=20).grid(row=1, column=0, sticky="e")
    userentry = Entry(loginframe, bg="#E9A178", fg="#4a3933", width=20, textvariable=userinfo)
    userentry.grid(row=1, column=1, sticky="w", padx=20)
    pwdentry = Entry(loginframe, bg="#E9A178", fg="#4a3933", width=20, show="*", textvariable=pwdinfo)
    pwdentry.grid(row=2, column=1, sticky="w", padx=20)
    Label(loginframe, text="Password  : ", bg="#F6E1C3", fg="#4a3933", padx=20).grid(row=2, column=0, sticky="e")
    Button(loginframe, text="Reset", width=15, command=resetclick).grid(row=3, column=0, pady=20, ipady=15, sticky="e", padx=20)
    Button(loginframe, text="Login", width=15, command=loginclick).grid(row=3, column=1, pady=20, ipady=15, sticky="w", padx=20)
    loginframe.grid(row=1, column=1, columnspan=2, rowspan=2, sticky="news")

def resetclick() :
    userentry.delete(0, END)
    pwdentry.delete(0, END)
    userentry.focus_force()

def loginclick() :
    status = check_login(userentry.get(), pwdentry.get())
    if status:
        welcomepage()
    else:
        messagebox.showerror(title="Unauthorized", message="Username or Password is invalid.")

def welcomepage() :
    global newframe
    newframe = Frame(root, bg="#E8D5C4")
    newframe.grid(row=1, column=1, columnspan=2, rowspan=2, sticky="news")
    newframe.rowconfigure((0,1,2,3,4), weight=1)
    newframe.rowconfigure(5, weight=2)
    newframe.columnconfigure((0,1), weight=1)
    Label(newframe, image=pic, bg="#E8D5C4").grid(row=0, column=0, columnspan=2, sticky="news")
    Label(newframe, text="Student ID", bg="#E8D5C4").grid(row=1, column=0, sticky="news")
    Label(newframe, text="Name", bg="#E8D5C4").grid(row=2, column=0, sticky="news")
    Label(newframe, text="Score", bg="#E8D5C4").grid(row=3, column=0, sticky="news")
    Label(newframe, text="Grade", bg="#E8D5C4").grid(row=4, column=0, sticky="news")

    Label(newframe, text=user_data[0], bg="#E8D5C4").grid(row=1, column=1, sticky="w")
    Label(newframe, text=user_data[1] +" "+ user_data[2], bg="#E8D5C4").grid(row=2, column=1, sticky="w")
    Label(newframe, text=user_data[3], bg="#E8D5C4").grid(row=3, column=1, sticky="w")
    Label(newframe, text=process_grade(user_data[3]), bg="#E8D5C4").grid(row=4, column=1, sticky="w")
    
    Button(newframe, text="Log Out", command=back2login).grid(row=5, columnspan=2)

def back2login() :
    newframe.grid_forget()
    loginpage(root)

def check_login(username, password) :    
    conn = sqlite3.connect("week10_1650705682.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Students WHERE username = ? AND password = ?", (username, password))
    global user_data
    user_data = cursor.fetchone()
    if user_data:
        return True
    else:
        return False
    
def process_grade(score) :
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

root = mainWindow()
pic = PhotoImage(file="images/profile.png").subsample(5,5)
userinfo, pwdinfo = StringVar(),StringVar()
loginpage(root)
root.mainloop()
