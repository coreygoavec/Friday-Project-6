from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("300x300")
# recongigure the size of the window so it doesn't shrink down

usernameFrame = Label(root, text = "Username")
usernameFrame.place(x = 70, y = 50)
usernameEntry = Entry(root)
usernameEntry.place(x = 150, y = 50)

passwordFrame = Label(root, text = "Password")
passwordFrame.place(x = 70, y = 70)
passwordEntry = Entry(root)
passwordEntry.place(x = 150, y = 70)

button1 = Button(root, text = "Login")
button1.place(x = 130, y = 100)

root.mainloop()