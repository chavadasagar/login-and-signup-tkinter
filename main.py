from email import message
from tkinter import *
from tkinter import messagebox
from dao import userdao

# loign and signup

def signup():
    global signup
    signup = Toplevel(home)
    signup.geometry("300x300")
    signup.title("Signup")

    
    global name,username,password
    name = StringVar(signup)
    username = StringVar(signup)
    password = StringVar(signup)


    # all function start here
    def saveUser():
        userdao.saveUser(name.get(),username.get(),password.get())
        messagebox.showinfo("successfylu!!!","user register success")
        
    def loginCommand():
        signup.destroy()
        login()
    def homeCommand():
        signup.destroy()
        home()
    # all function end 

    
    Label(signup,text="Signup",font="Arial 30").grid(row=0,column=0)

    Label(signup,text="").grid(row=1,column=0)
    
    Label(signup,text="Name :",font="Arial 10").grid(row=2,column=0)
    Entry(signup,relief="solid",bd=1,textvariable=name).grid(row=2,column=1)

    Label(signup,text="Username :",font="Arial 10").grid(row=3,column=0)
    Entry(signup,relief="solid",bd=1,textvariable=username).grid(row=3,column=1)

    Label(signup,text="Password :",font="Arial 10").grid(row=4,column=0)
    Entry(signup,relief="solid",bd=1,textvariable=password).grid(row=4,column=1)

    Label(signup,text="").grid(row=5,column=0)

    Button(signup,text="Signup",bd=1,relief="solid",font="arial 10",command=saveUser).grid(row=6,column=0)
    Button(signup,text="Login",bd=1,relief="solid",font="arial 10",command=loginCommand).grid(row=6,columnspan=2)
    Button(signup,text="Home",bd=1,relief="solid",font="arial 10",command=homeCommand).grid(row=6,column=1)
    
    signup.mainloop()

def login():
    global login
    login = Toplevel(home)
    login.geometry("300x300")
    login.title("Login")

    global username,password
    l_username = StringVar(login)
    l_password = StringVar(login)

    # all function start here
    def checkUser():
        if userdao.getUsernamePasswordByUser(l_username.get(),l_ password.get()):
            messagebox.showinfo("message","login success!!")
        else:
            messagebox.showinfo("message","wrong username or password")
    def loginCommand():
        login.destroy()
        signup()
    def homeCommand():
        login.destroy()
        home()
    # all function end

    
    Label(login,text="  Login  ",font="arial 30").grid(row=1,column=0)
    Label(login,text="").grid(row=1,column=0)
    Label(login,text="").grid(row=2,column=0)

    Label(login,text="Username :",font="arial 10").grid(row=3,column=0)
    Entry(login,bd=1,font="arial 10",relief="solid",textvariable=l_username).grid(row=3,column=1)

    Label(login,text="Password :",font="arial 10").grid(row=4,column=0)
    Entry(login,bd=1,font="arial 10",relief="solid",textvariable=l_password).grid(row=4,column=1)

    Label(login,text="").grid(row=5,column=0)
    Label(login,text="").grid(row=6,column=0)

    Button(login,text="Login",relief="solid",bd=1,command=checkUser).grid(row=6,column=0)
    Button(login,text="Signup",relief="solid",bd=1,command=loginCommand).grid(row=6,columnspan=2)
    Button(login,text="Home",relief="solid",bd=1,command=homeCommand).grid(row=6,column=1)

    login.mainloop()

def home():
    global home
    home = Tk()
    home.geometry("300x300")
    home.title("Home")

    Label(home,text="Home",bg="gray",font="arial 30",width=15).place(x=0,y=0)

    Button(home,text="Login",bd=1,relief="solid",font="arial 10",command=login).place(x=90,y=80)
    Button(home,text="Signup",bd=1,relief="solid",font="arial 10",command=signup).place(x=90,y=120)
    
    home.mainloop()


home()
