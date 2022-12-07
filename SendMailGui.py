from tkinter import *
from tkinter import Tk, Label, Frame, Entry, Button
import Mail as sm
import MainFrame as mf

def start():
    root = Tk()
    root.geometry('500x300')
    root.title("Registration Form")
    name = StringVar()
    Email = StringVar()
    
    label_1 = Label(root, text="Name", width=20, font=("bold", 15))
    label_1.place(x=35, y=80)     
    
    entry_1 = Entry(root, textvar=name)
    entry_1.place(x=240, y=80) 
    
    label_2 = Label(root, text="Email", width=20, font=("bold", 15))
    label_2.place(x=35, y=160)     
    
    entry_2 = Entry(root, textvar=Email)
    entry_2.place(x=240, y=160)
    
      
    def sendMail():
        Name=entry_1.get()
        email=entry_2.get()
        sm.send_email(Name,email)
        mf.start()
        
    Button(root, text="Send", width=20, bg='blue', fg='white', command=sendMail).place(x=180, y=230)
        
    root.mainloop()
    
 
#def sendMail():
#    sm.send_email(Name,email)
#    sm.send_email(name, email)    