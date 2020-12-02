from tkinter import *
import sqlite3


root = Tk()

root.minsize(300,200)

conn = sqlite3.connect("cred.db")
cursor=conn.cursor()
def login():
            global username , passwd
            string  = username.get()
            string2 = passwd.get()
            return string , string2
            
def find_user():
            string ,string2 = login()
            cursor.execute('SELECT * FROM credentials WHERE name = ? AND password = ?', (string, string2))
            if cursor.fetchone() is not None:
                print("Welcome you are logged in")
                new_w = Tk()
                root.minsize(300,200)
                label = Label(new_w , text="Welcome ")
                label.pack()
                mainloop()
            else:
                print("Please try again")

                
import db
label = Label(root , text="WELCOME" )
label.config(font = ("Firra Code" , 32))
label2 = Label(root , text="LOGIN")
label.config(font = ("Firra Code" , 20) , fg = "red")
userlabel = Label(root , text="username")
passwdlabel = Label(root , text="password")
username = Entry(root )
passwd = Entry(root , show = '*' )
loginbtn  =Button(root , text="LOGIN" , command = find_user , fg = "green" , bg = "yellow")
label.grid(row = 0 , column = 7)
label2.grid(row = 2 , column = 7)
userlabel.grid(row = 5,column=6 )
username.grid(row =5 , column =  7)
passwdlabel.grid(row =6 , column =6)
passwd.grid(row = 6 , column =7)
loginbtn.grid(row =7 , column =7)
            
     

mainloop()
            