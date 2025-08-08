import tkinter
from tkinter import *
tk = Tk()
tk.title("Mile to km Converter")
tk.config(padx=20,pady=20)

km = 0

def cal():
    global km
    km = round(float(enter.get()) * 1.609)
    kmm["text"] = km

label = tkinter.Label(text= f"is equal to")
label.grid(row=2,column=0)

label = tkinter.Label(text= f"Km")
label.grid(row=2,column=3)
label.config(pady=5,padx=5)

label = tkinter.Label(text= f"Miles")
label.grid(row=1,column=3)

kmm = tkinter.Label(text= f"0")
kmm.grid(row= 2, column=1)

enter = Entry(width=10)

enter.insert(0,0)
enter.grid(row= 1, column=1)
enter.focus()

button = Button(text="Calculate", command=cal)
button.grid(row= 3, column=1)


tk.mainloop()