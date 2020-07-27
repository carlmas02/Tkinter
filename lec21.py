from tkinter import *

root = Tk()
root.geometry("550x550")
root.title("listbox")

def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i += 1

i = 0
lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "My item")

Button(root,text = "add", command = add).pack()

root.mainloop()