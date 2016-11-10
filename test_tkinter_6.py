from tkinter import *
from tkinter.ttk import *

root = Tk()

def additem():
    items.set(items.get() + 1)

f = Frame(root)

items = IntVar()
items.set(14)

l0 = Label(f, text="I have")
l1 = Label(f, textvariable=items)
l2 = Label(f, text="items")

b = Button(root, text="Add item", command=additem)

l0.pack(side=LEFT)
l1.pack(side=LEFT)
l2.pack(side=LEFT)

f.pack()
b.pack()

root.mainloop()