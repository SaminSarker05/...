from tkinter import *

root = Tk()

root.title("Calculator")

#root.geometry("235x295")
root.geometry("500x500")
e = Entry(root).grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 0)
#e.pack()

num1 = Button(root, text = "1", padx = 20, pady = 20).grid(row = 4, column = 1)
num2 = Button(root, text = "2", padx = 20, pady = 20).grid(row = 4, column = 2)
num3 = Button(root, text = "3", padx = 20, pady = 20).grid(row = 4, column = 3)
num4 = Button(root, text = "4", padx = 20, pady = 20).grid(row = 3, column = 1)
num5 = Button(root, text = "5", padx = 20, pady = 20).grid(row = 3, column = 2)
num6 = Button(root, text = "6", padx = 20, pady = 20).grid(row = 3, column = 3)
num7 = Button(root, text = "7", padx = 20, pady = 20).grid(row = 2, column = 1)
num8 = Button(root, text = "8", padx = 20, pady = 20).grid(row = 2, column = 2)
num9 = Button(root, text = "9", padx = 20, pady = 20).grid(row = 2, column = 3)
num0 = Button(root, text = "0", padx = 48, pady = 20).grid(row = 5, column = 1, columnspan = 2)

deci = Button(root, text = ".", padx = 22, pady = 20).grid(row = 5, column = 3)

clear = Button(root, text = "AC", padx = 20, pady = 20).grid(row = 1, column = 1)
neg_pos = Button(root, text = "+/-", padx = 20, pady = 20).grid(row = 1, column = 2)
percent = Button(root, text = "%", padx = 20, pady = 20).grid(row = 1, column = 3)



div = Button(root, text = "/", padx = 20, pady = 20).grid(row = 1, column = 4)
times = Button(root, text = "*", padx = 20, pady = 20).grid(row = 2, column = 4)
minus = Button(root, text = "-", padx = 20, pady = 20).grid(row = 3, column = 4)
add = Button(root, text = "+", padx = 20, pady = 20).grid(row = 4, column = 4)
equal = Button(root, text = "=", padx = 20, pady = 20).grid(row = 5, column = 4)







root.mainloop()





























"""

from tkinter import *
from tkinter import ttk

root = Tk();
#root.title("Feet to Meters")

def click():
    label = Label(root, text = "Hello " + e.get())
    label.pack()

e = Entry(root, width = 50)
e.insert(0, "Username")
#borderwidth
#Entry.get() to text from input
#e.insert(index, "") - default vale for textbox
e.pack()

b = Button(root, text = "Click", padx = 50, command = click)
#fg = "", bg = ""
b.pack()
#main = ttk.Frame(root, padding = "10 10 10 10").grid(row = 0, column = 0)

#b = Button(root, text = "press", command = root.destroy)
#b.pack()


root.mainloop()
"""

