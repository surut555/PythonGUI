from tkinter import*

root = Tk()

myLabel1 = Label(root, text="Hello Word!")
myLabel2 = Label(root, text="My Name is surut setthanan")
myLabel3 = Label(root, text="                       ")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)


root.mainloop()