from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.title('โปรแกรมบันทึกความรู้จาก Uncle Lab')
GUI.geometry('500x400')


FONT1 = ('Angsana New', 30)
FONT2 = ('Angsana New', 15)

L = Label(GUI, text="กรอกความรู้ใหม่ไปลงไปในช่องว่าง", font=FONT1, fg='green')
L.pack(pady=5)

E1 = ttk.Entry(GUI, font=FONT2, width=40)
E1.pack(pady=2)


B1 = ttk.Button(GUI, text="บันทึก")
B1.pack(ipadx=15, ipady=10, pady=10)


L = Label(GUI, text="function คือ คล้ายกล้องที่เอาไว้เก็บคำสั่ง", font=FONT2, fg='black')
L.pack(pady=50)

B2 = ttk.Button(GUI, text="<", width=5)
B2.place(x=20, y=235)


B3 = ttk.Button(GUI, text=">", width=5)
B3.place(x=450, y=235)

GUI.mainloop()