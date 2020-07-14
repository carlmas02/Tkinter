from tkinter import *

#to pack we use .pack() or .grid()

main_root = Tk()

main_root.geometry("733x434")
main_root.title("carl")

#width,ht
main_root.minsize(500,600)

#IMPLABELS
#text - adds the text
#bd - background
#fg - foreground
#font - sts the font
#1.font =("comicsans",20,"bold")
#2.font =("comicsans 20 bold")
#padx - x padding
#pady - y padding
#relief - border styling - SUNKEN,RAISED,GROOVE,RIDGE
#Label
#PhotoImage
#Frame
#Button
#Entry = for typing something in a box
#Checkbutton
# .get() or .set() to get value

#info
title_label = Label(text="scratch.py", bg = "blue" ,font =("comicsans",10,"bold") , borderwidth = 3, relief = SUNKEN)
mainlabel = Label(text= "carls Edition")
photo = PhotoImage(file="C://Users//Iris//Downloads//placeholder.png")
photo_label = Label(image=photo)
photo_label.pack()
mainlabel.pack()


#import pack options
#anchor = nw
#fill = X or Y
#padx
#pady
#side = top,bottom,left,right

title_label.pack(anchor= "s")


#guilogic
main_root.mainloop()

#variable classes in tkinter
#boolean var, doublevar,intvar,stringvar

# .get() get a certain value
