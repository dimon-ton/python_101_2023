from tkinter import *
from tkinter import ttk
from tkinter import messagebox


import sqlite3

# Connect to the database (create it if it doesn't exist)
conn = sqlite3.connect('testdb.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a SQL statement
cursor.execute('''CREATE TABLE IF NOT EXISTS knowledge (id INTEGER PRIMARY KEY, topic TEXT, other TEXT)''')

def connect():
    """Create a connection to the database"""
    conn = sqlite3.connect('testdb.db')
    return conn


def create(conn, topic, other):
    """Insert a new record into the table"""
    conn = connect()
    cursor = conn.cursor()
    command = "INSERT INTO knowledge (topic, other) VALUES (?, ?)"
    cursor.execute(command, (topic, other))
    conn.commit()
    conn.close()



def read(conn):
    """Retrieve all records from the table"""

    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM knowledge")
    rows = cursor.fetchall()

    conn.close()

    return rows



current_knowledge = read(conn)

count = len(current_knowledge)-1


GUI = Tk()
GUI.title('โปรแกรมบันทึกความรู้จาก Uncle Lab')
GUI.geometry('500x400')


FONT1 = ('Angsana New', 30)
FONT2 = ('Angsana New', 15)

L = Label(GUI, text="กรอกความรู้ใหม่ไปลงไปในช่องว่าง", font=FONT1, fg='green')
L.pack(pady=5)

v_topic = StringVar()

E1 = ttk.Entry(GUI, textvariable=v_topic, font=FONT2, width=40)
E1.pack(pady=2)


def SaveTopic():
    topic = v_topic.get()
    create(conn, topic, '')
    
    messagebox.showinfo('หน้าต่างแสดงสถานะ', 'บันทึกข้อมูลเรียบร้อย')
    v_topic.set('')
    E1.focus()

    global current_knowledge
    current_knowledge = read(conn)

    

B1 = ttk.Button(GUI, text="บันทึก", command=SaveTopic)
B1.pack(ipadx=15, ipady=10, pady=10)

v_result = StringVar()
v_result.set(current_knowledge[count][1])

L = Label(GUI, textvariable=v_result, font=FONT2, fg='black')
L.pack(pady=50)



def Previous():
    global count
    index = count - 1
   
    if index >= 0:
        count = index
        v_result.set(current_knowledge[index][1])







B2 = ttk.Button(GUI, text="<", width=5, command=Previous)
B2.place(x=20, y=235)




def Next():
    global count
    index = count + 1
    
    
    if index <= len(current_knowledge)-1:
        count = index
        v_result.set(current_knowledge[index][1])




B3 = ttk.Button(GUI, text=">", width=5, command=Next)
B3.place(x=450, y=235)



GUI.mainloop()