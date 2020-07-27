from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")


if __name__ == "__main__":
    window = GUI()
    window.mainloop()