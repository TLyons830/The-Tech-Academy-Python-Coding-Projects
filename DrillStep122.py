import tkinter
from tkinter import filedialog
from tkinter import *
import os


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Ask Direcotry')

        self.txtvar = Entry(self.master, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtvar.grid(row=0, column=1, padx=(30,0), pady=(30,0))

        self.btnDir = Button(self.master, text="Ask Directory", width=10, height=2, command=self.askDir)
        self.btnDir.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)



    def askDir(self):
        fp = filedialog.askdirectory()
        self.txtvar.insert(0,"{}".format(fp))







if __name__  == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
