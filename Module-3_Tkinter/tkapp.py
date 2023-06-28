import tkinter
from tkinter import ttk,messagebox

window=tkinter.Tk()
window.title("FirstApp")
window.geometry("400x500")
window.config(background='gold')

"""tkinter.Label(text="Firstname:").pack()
tkinter.Label(text="Lastname:").pack()"""

"""tkinter.Label(text="Firstname:").place(x=0,y=0)
tkinter.Label(text="Lastname:").place(x=0,y=30)"""

tkinter.Label(text="Firstname:",bg='gold',font='Fixedsys 15',fg='red').grid(row=0,column=0,sticky='W')
tkinter.Label(text="Lastname:",bg='gold',font='Fixedsys 15',fg='red').grid(row=1,column=0,sticky='W')

tkinter.Entry(font='Fixedsys 15',fg='red').grid(row=0,column=1,sticky='W')
tkinter.Entry(font='Fixedsys 15',fg='red').grid(row=1,column=1,sticky='W')

tkinter.Radiobutton(value=0,text='Male',bg='gold',font='Fixedsys 15',fg='red').grid(row=2,column=0,sticky='W')
tkinter.Radiobutton(value=1,text='Female',bg='gold',font='Fixedsys 15',fg='red').grid(row=2,column=1,sticky='W')

tkinter.Checkbutton(text='Python',bg='gold',font='Fixedsys 15',fg='red').grid(row=3,column=0,sticky='W')
tkinter.Checkbutton(text='JAVA',bg='gold',font='Fixedsys 15',fg='red').grid(row=4,column=0,sticky='W')
tkinter.Checkbutton(text='PHP',bg='gold',font='Fixedsys 15',fg='red').grid(row=5,column=0,sticky='W')
tkinter.Checkbutton(text='Android',bg='gold',font='Fixedsys 15',fg='red').grid(row=6,column=0,sticky='W')

city=['Rajkot','Ahmedabad','Baroda','Surat','Jamnagar']

ttk.Combobox(values=city).grid(row=7,column=0)

def btnclick():
    #print("Button clicked")
    #messagebox.showerror(title="Error",message="Something went wrong..,Try again!")
    #messagebox.showinfo(title="Success",message="Signup Successfully!")
    #messagebox.showwarning(title="Warning",message="Your disk is full!")
    #messagebox.askokcancel(title="Download",message="Do you want to continue?")
    #messagebox.askquestion(title="Download",message="Do you want to continue?")
    #messagebox.askretrycancel(title="Download",message="Do you want to continue?")
    messagebox.askyesnocancel(title="Download",message="Do you want to continue?")

tkinter.Button(text='Submit',font='Fixedsys 15',fg='red',command=btnclick).place(x=175,y=250)


tkinter.mainloop()