from tkinter import *
import sqlite3


root = Tk()

root.minsize(300,100)

def login():
            import tkin2          
def register():
            import tkin3



label = Label(root , text="HOW DO YOU WANT TO LOGIN")
label.config(font = ("Times New Roman" ,16))
logbtn = Button(root , text="LOGIN" , command = login)
regbtn = Button(root , text="SIGNIN" , command = register)



label.grid(row =0, column = 7)
logbtn.grid(row =2 , column = 7)
regbtn.grid(row =3 , column =7)
root.mainloop()
