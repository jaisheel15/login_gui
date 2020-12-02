from tkinter import *

root = Tk()

root.minsize(300,100)

label = Label(root , text="welcome")
l2 = Label(root , text="hello")


label.grid(row = 0 , column =3)
label.config(font = ("Firra Code" , 40))
l2.grid(row = 2 , column =2)


root.mainloop()