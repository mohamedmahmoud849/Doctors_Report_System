from tkinter import *
from tkinter import Tk, Label, Frame, Entry, Button
import sqlite3
import Register as rg
import Login as ln

def registration():
    screen.destroy()
    rg.start()

def login():
    screen.destroy()
    ln.start()

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info + ".txt", "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Success!", fg="green", font=("calibri", 11)).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Homepage")
    Label(text="Select Your Choice", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Registration", height="2", width="30", command=registration).pack()

    screen.mainloop()


main_screen()