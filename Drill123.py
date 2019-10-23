import tkinter
from tkinter import filedialog
from tkinter import *
import os
import sqlite3
import sys 
import time
import shutil


class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__ (self, master, *args, **kwargs)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('1350x275')

        self.master.title('Drill 123')


        self.txtSource = Entry(self.master, font=("Helvetica", 19), fg='black', bg='white', width=75)
        self.txtSource.grid(row=0, column=1, columnspan =3, padx=(40,0), pady=(75,0), sticky=N)

        self.txtDestination = Entry(self.master, font=("Helvetica", 19), fg='black', bg='white', width=75)
        self.txtDestination.grid(row=1, column=1, columnspan =3, padx=(40,0), pady=(10,0), sticky=N)

        self.btnSource = Button(self.master, text="Source Directory", width=19, height=2, command=self.sourceDir)
        self.btnSource.grid(row=0, column=0, padx=(20,0), pady=(75,0), sticky=N+E+S+W)

        self.btnDestination = Button(self.master, text="Destination Directory", width=19, height=2, command=self.destDir)
        self.btnDestination.grid(row=1, column=0, padx=(20,0), pady=(10,0), sticky=N+E+S+W)

        self.btnIterate = Button(self.master, text="Move Text Files", width=19, height=3, command=self.MoveTextFiles)
        self.btnIterate.grid(row=2, column=0, padx=(20,0), pady=(15,0), sticky=S+W)




    def sourceDir(self):
        self.sfp = filedialog.askdirectory()
        self.txtSource.insert(0,"{}".format(self.sfp))

    def destDir(self):
        self.dfp = filedialog.askdirectory()
        self.txtDestination.insert(0,"{}".format(self.dfp))

    def MoveTextFiles(self):
        for file in os.listdir(self.sfp):
            if file.endswith(".txt"):
                SPath = os.path.join(self.sfp, file)
                self.DPath = shutil.move(SPath, self.dfp)

        conn = sqlite3.connect('Drill_123DB.db')
        with conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS tbl_TextFiles123 ( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_FileName STRING, \
                col_MTime)")
            conn.commit()
        conn.close()
        #conn = sqlite3.connect('Drill_123DB.db')
        #with conn:
            #cur = conn.cursor()
            #cur.execute("DELETE FROM tbl_TextFiles123")
            #conn.commit()
        #conn.close()
        
        for item in os.listdir(self.dfp):
            conn = sqlite3.connect('Drill_123DB.db')
            with conn:
                cur = conn.cursor()
                if item.endswith('.txt'):
                    abPath = os.path.join(self.dfp, item)
                    time_stamp = os.path.getmtime(abPath)
                    cur.execute("INSERT INTO tbl_TextFiles123(col_FileName, col_Mtime) VALUES (?, ?)", (item, time_stamp,))
                    conn.commit()
        conn.close()
 
        conn = sqlite3.connect('Drill_123DB.db')
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM tbl_TextFiles123")
            printStuff = cur.fetchall()
            print(printStuff)
        conn.close()
            








if __name__  == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
