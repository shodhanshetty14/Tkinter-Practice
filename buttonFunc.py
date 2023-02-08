from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Click me If you can")
root.geometry("500x500")
content = ttk.Frame(root)

label1 = Label(root, text="Try Clicking me!!")
label1.pack()

button = Button(root, text="Click me", command=lambda: button.config(text="You clicked me!!"))
button.pack()

if __name__ == "__main__":
    root.mainloop()