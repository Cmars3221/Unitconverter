from tkinter import *

kilo = Tk()

def kilos_getit():
    grams = int(entry_value.get())*1000
    pounds = float(entry_value.get())*2.20462
    ounces = float(entry_value.get())*35.274
    t1.insert(END,grams)
    t2.insert(END,pounds)
    t3.insert(END,ounces)

button=Button(kilo,text="Caluclate",command=kilos_getit)
button.grid(row=0,column=1)


entry_value = StringVar()
entry_box=Entry(kilo,textvariable=entry_value)
entry_box.grid(row=0,column=2)

t1=Text(kilo,height=1, width=20)
t1.grid(row=1,column=0)

t2=Text(kilo,height=1, width=20)
t2.grid(row=1,column=1)

t3=Text(kilo,height=1, width=20)
t3.grid(row=1,column=2)




kilo.mainloop()
