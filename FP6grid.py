from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("300x300")
# recongigure the size of the window so it doesn't shrink down

nameFrame = Label(root, text = "Name")
nameFrame.grid(column = 10)

emailFrame = Label(root, text = "Email")
emailFrame.grid(column = 10)

passwordFrame = Label(root, text = "Password")
passwordFrame.grid(column = 10)

button1 = Button(root, text = "Sign Up Now")
button1.grid(column = 10)

root.mainloop()