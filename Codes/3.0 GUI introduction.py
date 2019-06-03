import tkinter as tk

window=tk.Tk() #creating the main window

def func1():
    
    label1.config(text='HELLO PYTHON',bg='blue')
    button1.config(fg='green')

def func2():
    
    label1.config(text='HELLO TKINTER',bg='hot pink')

#window.mainloop()

font1='Helvetica 20 bold'
font2='Times 15 bold'

label1=tk.Label(window,text='HELLO TKINTER!',bg='hot pink',fg='white',font=font1)
label1.grid(row=0,column=0) #positioning the label1 from grid method

button1=tk.Button(window,text='CHANGE',bg='red',fg='gray80',font=font2,height=2,width=10,command=func1)
button1.grid(row=1,column=0)

button2=tk.Button(window,text='CHANGE',bg='green',fg='gray80',font=font2,height=2,width=10,command=func2)
button2.grid(row=1,column=1)
