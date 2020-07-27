from tkinter import *
root = Tk()
root.geometry("500x400")

user = Label(root, text = "Username")
password = Label(root, text = "Password")

def getsvals():
    if uservalue.get() == "carl" and passvalue.get() == "mas":
        print("WELCOME SIR")
    else:
        print("opps!!Please check ur username or password.")

user.grid()
password.grid()

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable = uservalue)
passentry = Entry(root, textvariable = passvalue)

userentry.grid(row = 0 , column = 1)
passentry.grid(row = 1 , column = 1)

Button(text = "SUBMIT" , command = getsvals ).grid()


root.mainloop()