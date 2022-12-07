from tkinter import *
from tkinter import Tk, Button
import ReportWritergui as rw
import SendMailGui as smg
import reportsgui as rg
def makereport():
    rw.reportwritter()

def sendmail():
    smg.start()
    
    
def showreports():
    rg.start()   

def start():
    root = Tk()
    root.geometry('500x500')
    root.title("Report system")

    label_0 = Label(root, text="Welcome Doctor", width=20, font=("bold", 20))
    label_0.place(x=90, y=45)

    Button(root, text="Make a report", width=20, bg='blue',fg="white", command=makereport ).place(x=180, y=120)
    Button(root, text="Show reports", width=20, bg='blue', fg="white", command=showreports).place(x=180, y=200)

    Button(root, text="Send a report", width=20, bg='blue', fg="white" , command=sendmail).place(x=180, y=280)

    root.mainloop()
