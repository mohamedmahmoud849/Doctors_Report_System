from tkinter import *
from tkinter import Tk, Button, Label, Frame
import ReportWriter as rw
import voiceRecognitio as vr
import MainFrame as mf





def reportwritter():
   
    root = Tk()
    root.geometry('800x700')
    root.title("Report system")
    name = StringVar()
    Email = StringVar()
    
    label_1 = Label(root, text="Name", width=20, font=("bold", 15))
    label_1.place(x=60, y=80)     
    
    entry_1 = Entry(root, textvar=name)
    entry_1.place(x=265, y=80) 
    
    label_2 = Label(root, text="Email", width=20, font=("bold", 15))
    label_2.place(x=60, y=160)     
    
    entry_2 = Entry(root, textvar=Email)
    entry_2.place(x=265, y=160)
    def voiceRecognition():
        vr.flag=1
        Name=entry_1.get()
        email=entry_2.get()
        vr.ask(Name,email)
        mf.start()
    

    label_0 = Label(root, text="To start recording report press the below button", font=("bold", 20))
    label_0.place(x=115, y=220)

    Button(root, text="Start recording", width=20, bg='white', fg="black" , command=voiceRecognition).place(x=205, y=320)
    button_quit = Button(root, text="Exit program", command=root.quit)
    button_quit.pack()

    root.mainloop()


