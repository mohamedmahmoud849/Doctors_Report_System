from tkinter import *
from tkinter import Tk, Label, Frame, Entry, Button, ttk
import sqlite3
from tkinter import *


def start():
    wind =Tk()
    wind.geometry("1000x700")
    wind.title("Homepage")
    Patemail = StringVar()
    label_2 = Label(wind, text="Patient email", width=20, font=("bold", 12))
    label_2.place(x=100, y=480)
    entry_2 = Entry(wind, textvar=Patemail)
    entry_2.place(x=290, y=480)
    wind.title('Patients records')
    tree = ttk.Treeview( wind,height=10, columns=("2", "3", "4", "5", "6", "7", "8", "9", "10", "11"))
    tree.grid(row=20, column=0, columnspan=20)
    tree.grid_rowconfigure(0, weight=1)
    tree.column('#0', stretch=NO, minwidth=0, width=100)
    tree.column('2', stretch=NO, minwidth=0, width=100)
    tree.column('3', stretch=NO, minwidth=0, width=100)
    tree.column('4', stretch=NO, minwidth=0, width=100)
    tree.column('5', stretch=NO, minwidth=0, width=100)
    tree.column('6', stretch=NO, minwidth=0, width=100)
    tree.column('7', stretch=NO, minwidth=0, width=100)
    tree.column('8', stretch=NO, minwidth=0, width=100)
    tree.column('9', stretch=NO, minwidth=0, width=100)
    tree.column('10', stretch=NO, minwidth=0, width=100)
    tree.column('11', stretch=NO, minwidth=0, width=100)
    tree.heading('#0', text='Patient name', anchor=W)
    tree.heading(2, text='email', anchor=W)
    tree.heading(3, text='admitted date', anchor=W)
    tree.heading(4, text='Reason for admission', anchor=W)
    tree.heading(5, text='Past history', anchor=W)
    tree.heading(6, text='Progress', anchor=W)
    tree.heading(7, text='Current condition', anchor=W)
    tree.heading(8, text='Prognosis', anchor=W)
    tree.heading(9, text='lab results', anchor=W)
    tree.heading(10, text='Current medication', anchor=W)
    tree.heading(11, text='arrangements', anchor=W)
    def searchReport(email):
        conn = sqlite3.connect('Hospital.db')
        raws = []
        with conn:
            cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM Reports WHERE Email = ?', [email])
        results = cursor.fetchall()
        for raw in results:
            raws.append(raw)
        conn.commit()
        return results
    def view():
        tree.insert
        db_rows = searchReport(entry_2.get())
        for row in db_rows:
            tree.insert('', 0, text=row[0],
                        values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))

    Button(wind, text="Search", width=18, bg='white', fg="black",
            command=view).place(x=300, y=580)



    wind.mainloop()






