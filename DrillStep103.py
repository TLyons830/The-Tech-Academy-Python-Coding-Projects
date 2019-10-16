import sqlite3


fileList = ('information.docx', 'Hello.txt','myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


conn = sqlite3.connect('DrillStep103DB.db')


with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_TextFiles ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_FileName STRING)")
    conn.commit()
conn.close()


#conn = sqlite3.connect('DrillStep103DB.db')

#with conn:
 #   cur = conn.cursor()
  #  cur.execute("DELETE FROM tbl_TextFiles")
   # conn.commit()
#conn.close()


conn = sqlite3.connect('DrillStep103DB.db')


with conn:
    cur = conn.cursor()
    for item in fileList:
        if item.endswith('.txt'):
            cur.execute("INSERT INTO tbl_TextFiles(col_FileName) VALUES (?)", (item,))
            conn.commit()
conn.close()



conn = sqlite3.connect('DrillStep103DB.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_FileName FROM tbl_TextFiles")
    varFileName = cur.fetchall()
    print(varFileName)
conn.close()

