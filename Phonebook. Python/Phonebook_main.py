from tkinter import *
from tkinter import messagebox
import tkinter as tk

import Phonebook_gui
import Phonebook_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)

        Phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook")
        self.master.configure(bg="#F0F0F0")

        self.master.protocol("WM_DELETE_WINDOW", lambda: Phonebook_func.ask_quit(self))
        arg = self.master

        Phonebook_gui.load_gui(self)

        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: Phonebook_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About this phonebook demo")
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.master.config(menu=menubar, borderwidth='1')

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

