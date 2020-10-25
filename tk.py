import tkinter as tk
from tkinter import *
from tkinter import ttk

class myWin(Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Title")

        self.label1 = Label(self, text="This is text", width=50, bd=5, pady=10, bg="#789", fg="#f00")
        self.label1.grid(row=2, column = 1)
        self.button1 = Button( self, text = "CLICK HERE", width = 25)
        self.button1.grid( row = 3, column = 2, columnspan = 1, sticky = W+E+N+S )
def main():
    myWin().mainloop()

main()