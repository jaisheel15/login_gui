import db
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
            cursor.execute('insert into credentials  (name, password) VALUES (?, ?)', (string, string2))
            conn.commit()



label = Label(root , text="WELCOME" )
label.config(font = ("Firra Code" , 40))
label2 = Label(root , text="LOGIN")
label.config(font = ("Firra Code" , 20) , fg = "red")
userlabel = Label(root , text="username")
passwdlabel = Label(root , text="password")
username = Entry(root )
passwd = Entry(root )
loginbtn  =Button(root , text="LOGIN" , command = find_user , fg = "green" , bg = "yellow")
label.grid(row = 0 , column = 8)
label2.grid(row = 2 , column = 8)
userlabel.grid(row = 5,column=7 )
username.grid(row =5 , column =  8)
passwdlabel.grid(row =6 , column =7)
passwd.grid(row = 6 , column =8)
loginbtn.grid(row =8 , column =8)
            
     

mainloop()
            