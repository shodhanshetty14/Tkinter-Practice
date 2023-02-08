from faulthandler import disable
from sre_parse import State
from tkinter import *

root = Tk()
root.title("Grids")
root.geometry("500x500")
# we are creating the label to be displayed
My_Label1 = Label(root, text="Hello Everyone Im Shodhan  Shetty. ")
My_Label2 = Label(root, text="Yeah I'm Studying Python").grid(row=0, column=1)

My_Label1.grid(column=0, row=0)
# My_Label2.grid(column=0, row=1)

def location():
    from random import randint
    x = randint(10, 500)
    y = randint(10, 500)
    My_button.place_configure(x=x, y=x)


# My_button = Button(root, text="Click me", command=location).grid(row=1, column=1)
# My_button['command'] = lambda w=My_button: location(w)
My_button = Button(root, text="Click me", command=location)
My_button.place(x = 200, y = 200)

root.mainloop()

