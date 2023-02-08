from tkinter import *

root = Tk()
input_space = Entry(root, width = 50, borderwidth=5)
input_space.insert(0, "Enter Your Name")
input_space.pack()


def MyClick():
    mssg = Label(root, text=f"Hello { input_space.get()}. Welcome back")
    mssg.pack()

my_button = Button(root, text ="Enter Your Name",  state=DISABLED, fg = "white", bg = "black")
my_button.pack()
# 'fg' changes the color of the button text, 'bg' changes the color of the button
# for coloring we can also use the hex color code

btn = Button(root, text="Submit", padx=30, pady=20, command=MyClick)
btn.pack()

root.mainloop()
