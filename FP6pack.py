from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x500")
# recongigure the size of the window so it doesn't shrink down

entryBox = Entry(root, state = 'disabled')
entryBox.pack()

# Buttons for numbers and operators

button1 = ttk.Button(root, text = "1")
button1.pack()

button2 = ttk.Button(root, text = "2")
button2.pack()

button3 = ttk.Button(root, text = "3")
button3.pack()

button4 = ttk.Button(root, text = "4")
button4.pack()

button5 = ttk.Button(root, text = "5")
button5.pack()

button6 = ttk.Button(root, text = "6")
button6.pack()

button7 = ttk.Button(root, text = "7")
button7.pack()

button8 = ttk.Button(root, text = "8")
button8.pack()

button9 = ttk.Button(root, text = "9")
button9.pack()

buttonPlus = ttk.Button(root, text = "+")
buttonPlus.pack()

buttonMinus = ttk.Button(root, text = "-")
buttonMinus.pack()

buttonMult = ttk.Button(root, text = "*")
buttonMult.pack()

buttonDiv = ttk.Button(root, text = "/")
buttonDiv.pack()

root.mainloop()