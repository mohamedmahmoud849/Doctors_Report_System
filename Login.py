from tkinter import *
from tkinter import Tk, Label, Frame, Entry, Button
import sqlite3
import MainFrame as mf

def start():
    root = Tk()
    root.geometry('500x500')
    root.title("LogIn")
    Fullname = StringVar()
    Email = StringVar()
    Password = StringVar()
    Department = StringVar()
    Phone = StringVar()

    label_0 = Label(root, text="LogIn", width=20, font=("bold", 20))
    label_0.place(x=90, y=53)

    label_1 = Label(root, text="Email", width=20, font=("bold", 10))
    label_1.place(x=80, y=130)

    entry_1 = Entry(root, textvar=Fullname)
    entry_1.place(x=240, y=130)

    label_2 = Label(root, text="Password", width=20, font=("bold", 10))
    label_2.place(x=68, y=180)

    entry_2 = Entry(root, textvar=Password)
    entry_2.place(x=240, y=180)

    # Button(root,text="Submit",width=20,bg='blue',fg="white",command=database).place(x=180,y=380)

    def login():
        username = entry_1.get()
        password = entry_2.get()
        conn = sqlite3.connect('Hospital.db')

        with conn:
            cursor = conn.cursor()

            cursor.execute('SELECT Email , Password FROM Users  WHERE EMAIL = ? AND Password = ?',
                           (username, password))
            result = cursor.fetchall()
            if len(result) == 0:
                Label( root, text="Invalid username or password", fg="red", font=("calibri", 11)).pack()
            else:
                root.destroy()
                mf.start()

        conn.commit()

    Button(root, text="Log In", width=20, bg='blue', fg="white", command=login).place(x=180, y=380)

    root.mainloop()
