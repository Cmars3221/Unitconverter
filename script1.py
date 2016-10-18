from tkinter import *

window = Tk()

def km_to_miles():
    # print(e1_value.get())
    miles = float(e1_value.get())*1.6
    t1.insert(END,miles)   #input param(miles) the end of feld t1.
                           #insert is proprietary function of tkinter.

b1=Button(window,text="blah",command=km_to_miles)
b1.grid(row=0,column=0)
                             #command is the function link, leave out ().

e1_value=StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1= Text(window, heigh=2, width=20)\
t1.grid(row=0,column=2)

window.mainloop()       #leave this here so window state stays in op state.
