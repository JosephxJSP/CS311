import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def connection() :
    global conn,cursor
    conn = sqlite3.connect("database/login.db")
    cursor = conn.cursor()

def mainwindow() :
    root = Tk()
    w = 1200
    h = 800
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#28b5b5')
    root.title("Week12 Login/Update Application: ")
    root.option_add('*font',"Garamond 24 bold")
    root.rowconfigure((0,3),weight=1)
    root.rowconfigure((1,2),weight=2)
    root.columnconfigure((0,3),weight=1)
    root.columnconfigure((1,2),weight=2)
    return root

def loginlayout() :
    global userentry,pwdentry
    loginframe.rowconfigure((0,1,2,3),weight=1)
    loginframe.columnconfigure((0,1),weight=1)
    loginframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')
    Label(loginframe,text="Account Login",font="Garamond 26 bold",image=img3,compound=LEFT,bg='#8fd9a8',fg='#e4fbff').grid(row=0,columnspan=2)
    Label(loginframe,text="Username : ",bg='#8fd9a8',fg='#e4fbff',padx=20).grid(row=1,column=0,sticky='e')
    userentry = Entry(loginframe,bg='#e4fbff',width=20)
    userentry.grid(row=1,column=1,sticky='w',padx=20)
    pwdentry = Entry(loginframe,bg='#e4fbff',width=20,show='*')
    pwdentry.grid(row=2,column=1,sticky='w',padx=20)
    Label(loginframe,text="Password  : ",bg='#8fd9a8',fg='#e4fbff',padx=20).grid(row=2,column=0,sticky='e')
    Button(loginframe,text="Login",width=10,command=lambda:loginclick(userentry.get(),pwdentry.get())).grid(row=3,column=1,pady=20,ipady=15,sticky='e',padx=40)
    Button(loginframe,text="Exit",width=10,command=root.quit).grid(row=3,column=0,pady=10,ipady=15,sticky='w',padx=45)

def loginclick(user,pwd) :
    global result
    if user == "" or pwd == "" :
        messagebox.showwarning("Admin : ","Please enter a username or password")
        userentry.focus_force()
    else :
        sql = "select * from student where username=?;"
        cursor.execute(sql,[user])
        result = cursor.fetchone()
        if result :
            sql = "select * from student where username=? and password=?;"
            cursor.execute(sql,[user,pwd])
            result = cursor.fetchone()
            if result :
                messagebox.showinfo("Admin : ","Login Successfully.")
                welcomepage(result)
            else :
                messagebox.showwarning("Admin : ","Incorrect Password \nPlease try again")
                pwdentry.selection_range(0,END)
                pwdentry.focus_force()
        else :
            messagebox.showwarning("Admin : ","The username not found.")
            userentry.selection_range(0,END)
            userentry.focus_force()


def welcomepage(result) :
    print(result)
    loginframe.grid_forget()
    pwdframe.grid_forget()
    updateframe.grid_forget()
    welcomeframe['bg'] = "#FCC2FC"
    welcomeframe.grid_rowconfigure((0,1,2,3,4,5,6),weight=1)
    welcomeframe.grid_columnconfigure((0,1),weight=1)
    welcomeframe.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='news')
    Label(welcomeframe,image=img1,bg='#FCC2FC').grid(row=0,columnspan=2)
    title = ['Student ID :','First Name :','Last Name','Gender :','Year : ']
    for i,data in enumerate(title) :
        Label(welcomeframe,bg='#FCC2FC',text=data).grid(row=i+1,column=0,sticky='e')
        Label(welcomeframe,bg='#FCC2FC',text=result[i]).grid(row=i+1,column=1,padx=10,sticky='w',ipadx=100)
    Button(welcomeframe,text="Change a Password",width=20,command=changeclick).grid(row=i+2,columnspan=2,sticky='w',padx=20,ipady=15)
    Button(welcomeframe,text="Update a Student Name",width=20,command=updateclick).grid(row=i+2,columnspan=2,ipady=15)
    Button(welcomeframe,text="Log Out",width=15,command=logoutclick).grid(row=i+2,columnspan=2,sticky='e',padx=20,ipady=15)
    
def logoutclick() :
    loginlayout() 
    welcomeframe.grid_forget()
    pwdframe.grid_forget()
    updateframe.grid_forget()

def changeclick() :
    global newpwd,cfpwd
    welcomeframe.grid_forget()
    updateframe.grid_forget()
    loginframe.grid_forget()
    pwdframe.grid_columnconfigure((0,1),weight=1)
    pwdframe.grid_rowconfigure((0,1,2,4,5),weight=1)
    pwdframe.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='news')
    Label(pwdframe,image=img1,bg='#28b5b5',text=result[1]+" "+result[2],compound='left').grid(row=0,columnspan=2)
    Label(pwdframe,text="New Password : ",bg='#28b5b5').grid(row=2,column=0,sticky='e',padx=15)
    newpwd = Entry(pwdframe,bg='#e4fbff',width=20,show='*')
    newpwd.grid(row=2,column=1,sticky='w',padx=15)
    Label(pwdframe,text="Confirm Password : ",bg='#28b5b5').grid(row=3,column=0,sticky='e',padx=15)
    cfpwd = Entry(pwdframe,bg='#e4fbff',width=20,show='*')
    cfpwd.grid(row=3,column=1,sticky='w',padx=15)
    Button(pwdframe,text="Confirm Click",width=15,command=lambda:changepwd(newpwd.get(),cfpwd.get())).grid(row=4,column=0,sticky='e',padx=30,ipady=15)
    Button(pwdframe,text="Back to Login",width=15,command=logoutclick).grid(row=4,column=1,sticky='w',padx=30,ipady=15)

def changepwd(newpass,cfpass) :
    if newpass == "" or cfpass == "" :
        messagebox.showwarning("Admin : ","Please enter a new password and a confirm password")
        newpwd.focus_force()
    else :
        if newpass == cfpass :
            #define sql command or sql statement for searching
            sql = "update student set password=? where username=?;"
            #execute sql using cursor
            cursor.execute(sql,[newpass,userentry.get()])
            #confirm/save data updated using commit() method
            conn.commit()
            messagebox.showinfo("Admin : ","Password update successfully")
            newpwd.delete(0,END)
            cfpwd.delete(0,END)
        else :
            messagebox.showwarning("Admin : ","A confirm password is not correct/Try again")
            cfpwd.select_range(0,END)
            cfpwd.focus_force()

def updateclick() :
    global searchbox,updatefnamebox,updatelnamebox
    welcomeframe.grid_forget()
    pwdframe.grid_forget()
    loginframe.grid_forget()
    updateframe.grid_columnconfigure(0,weight=1)
    updateframe.grid_columnconfigure(1,weight=1)
    updateframe.grid_columnconfigure(2,weight=1)
    updateframe.grid_rowconfigure((0,1,2,3,4,5,6,7,8),weight=1)
    
    updateframe.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='news')
    selectoption.set("Username")
    OptionMenu(updateframe,selectoption,"Username","First Name","Last Name").grid(row=1,sticky="s",column=0)
    searchbox = Entry(updateframe,width=25,bg="#C9F4AA",justify='right')
    searchbox.grid(row=1,sticky="sw",column=1,padx=15)
    Button(updateframe,image=img2,command=searchclick).grid(row=1,column=2,sticky='sw')
    Label(updateframe,text="First Name : ",bg="#E5FDD1").grid(row=2,column=2,columnspan=2)
    Label(updateframe,text="Last Name : ",bg="#E5FDD1").grid(row=4,column=2,columnspan=2)
    updatefnamebox = Entry(updateframe,width=25,bg="#ECF9FF",justify='left')
    updatefnamebox.grid(row=3,column=2,columnspan=2)
    updatelnamebox = Entry(updateframe,width=25,bg="#ECF9FF",justify='left')
    updatelnamebox.grid(row=5,column=2,columnspan=2)
    Button(updateframe,text="Update",width=6,command=updatesubmitclick).grid(row=6,column=2,sticky='w',ipady=10,padx=20)
    Button(updateframe,text="Delete",width=6,command=deleteclick).grid(row=6,column=2,sticky='e',ipady=10,padx=20)
    Button(updateframe,text="Logout",width=7,command=logoutclick).grid(row=6,column=3,sticky='w',ipady=10,padx=20)

def searchclick() : 
    if selectoption.get() == "Username" :
        # print(optiondata)
        # define sql command for searching a username
        sql = "select * from student where username=?"
    elif selectoption.get() == "First Name" :
        #print(optiondata)
        #define sql command for searching a first name
        sql = "select * from student where first_name=?"
    else :
        #print(optiondata)
        #define sql command for searching a last name
        sql = "select * from student where last_name=?"

    #execute sql using cursor
    cursor.execute(sql, [searchbox.get()])
    #fetch result
    result = cursor.fetchall()

    #delete all item from tree view
    for item in mytree.get_children():
        mytree.delete(item)
    if result :
        #print(result)
        #replace a treeview for display all data after searching
        mytree.grid(row=2,rowspan=5,column=0,columnspan=2)
        #define heading consist of (Student ID, Username, First Name, Last Name)
        #method heading() use to defind a treeview heading
        mytree.heading("col1", text="Student ID")
        mytree.heading("col2", text="Username")
        mytree.heading("col3", text="First Name")
        mytree.heading("col4", text="Last Name")
        #config columns using column() method which a column amount are equal to a heading columns
        mytree.column("col1", width=100, anchor="center")
        mytree.column("col2", width=100, anchor="center")
        mytree.column("col3", width=150)
        mytree.column("col4", width=150)
        mytree.column("#0",width=0,minwidth=0)          # Hidden Column 0
        #insert a record datas into a treeview (row by row) using for loop 
        for i,record in enumerate(result) :
            print("Data",record[0],record[1],record[2],record[3],record[4],record[5])
            # row = (record[0],record[1],record[2],record[3],record[4],record[5])
            mytree.insert('','end',values=(record[0],record[5],record[1],record[2]))        
        #take a user action (double click) 
        mytree.bind('<Double-1>',treeviewclick)
    else : 
        messagebox.showinfo("Admin : ","The "+selectoption.get()+" is not found\ntry again")
        updatefnamebox.delete(0,END)
        updatelnamebox.delete(0,END)
        searchbox.delete(0,END)
        for item in mytree.get_children():
            mytree.delete(item)
        mytree.grid_forget()

def treeviewclick(e) :
    global clickdata
    selectrow = mytree.selection()
    print("Mytree selection -> ",selectrow)
    clickdata = mytree.item(mytree.selection(),'values')
    print("Clickdata",clickdata)
    #insert data into entry box of first name and last name
    updatefnamebox.delete(0, END)
    updatelnamebox.delete(0, END)
    updatefnamebox.insert(0, clickdata[2])
    updatelnamebox.insert(0, clickdata[3])


def updatesubmitclick() :
    if updatefnamebox.get() != "" and updatelnamebox != "" :
        #define sql command or sql statement for updating
        sql = "UPDATE student SET first_name=?, last_name=? WHERE std_id=?"
        #execute sql using cursor
        cursor.execute(sql, [updatefnamebox.get(), updatelnamebox.get(), clickdata[0]])
        #confirm/save data updated using commit() method
        conn.commit()
        messagebox.showinfo("Admin : ","Update Successuflly.")
        updatefnamebox.delete(0,END)
        updatelnamebox.delete(0,END)
        searchbox.delete(0,END)
        for item in mytree.get_children():
            mytree.delete(item)
        mytree.grid_forget()
    else :
        messagebox.showwarning("Admin : ","First name or Last name is empty \n Please try again")
        searchbox.focus_force()

def deleteclick() :
    cf = messagebox.askquestion("Admin : ","Confirm to delete (Yes/No)")
    if cf == 'yes' :
        #define sql command or sql statement for deletion
        sql = "DELETE FROM student WHERE std_id=?"
        #execute sql using cursor
        cursor.execute(sql, [clickdata[0]])
        #confirm/save data updated using commit() method
        conn.commit()
        messagebox.showinfo("Admin : ","Delete Successfully")
        updatefnamebox.delete(0,END)
        updatelnamebox.delete(0,END)
        searchbox.delete(0,END)
        for item in mytree.get_children():
            mytree.delete(item)
        mytree.grid_forget()

connection()
root = mainwindow()
loginframe = Frame(root,bg='#8fd9a8')
welcomeframe = Frame(root,bg='#FCC2FC')
updateframe = Frame(root,bg="#E5FDD1")
mytree = ttk.Treeview(updateframe,columns=("col1","col2","col3","col4"))
pwdframe = Frame(root,bg='#28b5b5')
selectoption = StringVar()
img1 = PhotoImage(file='images/profile.png').subsample(5,5)
img2 = PhotoImage(file='images/search.png')
img3 = PhotoImage(file="images/login.png").subsample(6,6)
loginlayout()
root.mainloop()
cursor.close()
conn.close()