from tkinter import *
from tkinter import Tk, Label, Frame, Entry, Button
import tkinter
import sqlite3

def start():
    root = Tk()
    root.geometry('500x500')
    root.title("Registration Form")
    Fullname = StringVar()
    Email = StringVar()
    Password = StringVar()
    Department = StringVar()
    Phone = StringVar()

    label_0 = Label(root, text="Registration form", width=20, font=("bold", 20))
    label_0.place(x=90, y=53)

    label_1 = Label(root, text="Fullname", width=20, font=("bold", 10))
    label_1.place(x=80, y=130)

    entry_1 = Entry(root, textvar=Fullname)
    entry_1.place(x=240, y=130)

    label_2 = Label(root, text="Password", width=20, font=("bold", 10))
    label_2.place(x=68, y=180)

    entry_2 = Entry(root, textvar=Password)
    entry_2.place(x=240, y=180)

    label_3 = Label(root, text="Email", width=20, font=("bold", 10))
    label_3.place(x=70, y=230)

    entry_3 = Entry(root, textvar=Email)
    entry_3.place(x=240, y=230)

    label_4 = Label(root, text="Department", width=20, font=("bold", 10))
    label_4.place(x=70, y=280)

    entry_4 = Entry(root, textvar=Department)
    entry_4.place(x=240, y=280)

    label_5 = Label(root, text="Phone", width=20, font=("bold", 10))
    label_5.place(x=85, y=330)

    entry_5 = Entry(root, textvar=Phone)
    entry_5.place(x=240, y=330)

    def database():
        fullname = entry_1.get()
        email = entry_3.get()
        password = entry_2.get()
        department = entry_4.get()
        phone = entry_5.get()
        conn = sqlite3.connect('Hospital.db')
        with conn:
            cursor = conn.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS Users (Fullname TEXT,Email TEXT,Password TEXT,Department TEXT,Phone TEXT)')
        cursor.execute('INSERT INTO Users (FullName,Email,Password,Department,Phone) VALUES(?,?,?,?,?)',
                       (fullname, email, password, department, phone))
        conn.commit()
        Label( root, text="Registration Success!", fg="green", font=("calibri", 11)).pack()

    Button(root, text="Submit", width=20, bg='blue', fg='white',
           command=database).place(x=180, y=380)

    root.mainloop()
