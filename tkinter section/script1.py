from tkinter import *

window=Tk()

def kilo_to_mile():
    t1.insert(END,int(float(e1_value.get())*0.6214))

b1=Button(window,text='Execute',command=kilo_to_mile)
b1.grid(row=2,column=3)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=0)

t1=Text(window,height=1,width=20,)
t1.grid(row=0,column=2)

window.mainloop()