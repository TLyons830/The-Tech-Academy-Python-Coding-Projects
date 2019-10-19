import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('725x275')

        self.master.title('Check Files')

        self.varBrowse1 = StringVar()
        self.varBrowse2 = StringVar()

        self.txtBrowse1 = Entry(self.master,text=self.varBrowse1, font=("Helvetica", 19), fg='black', bg='white', width=35)
        self.txtBrowse1.grid(row=0, column=1, columnspan =3, padx=(40,0), pady=(75,0), sticky=N)

        self.txtBrowse2 = Entry(self.master,text=self.varBrowse2, font=("Helvetica", 19), fg='black', bg='white', width=35)
        self.txtBrowse2.grid(row=1, column=1, columnspan =3, padx=(40,0), pady=(10,0), sticky=N)

        self.btnBrowse1 = Button(self.master, text="Browse...", width=19, height=2)
        self.btnBrowse1.grid(row=0, column=0, padx=(20,0), pady=(75,0), sticky=N+E+S+W)

        self.btnBrowse2 = Button(self.master, text="Browse...", width=19, height=2)
        self.btnBrowse2.grid(row=1, column=0, padx=(20,0), pady=(10,0), sticky=N+E+S+W)

        self.btnCheck = Button(self.master, text="Check for Files...", width=19, height=3)
        self.btnCheck.grid(row=2, column=0, padx=(20,0), pady=(15,0), sticky=S+W)

        self.btnClose = Button(self.master, text="Close Program", width=18, height=3)
        self.btnClose.grid(row=2, column=3, padx=(0,0), pady=(0,0,), sticky=E+S)










if __name__  == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
