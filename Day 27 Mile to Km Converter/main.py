import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)


def convert(): 
    mile = int(ip.get())
    km.config(text=f"{1.6*mile}")

tk.Label(text="is equal to").grid(row=1,column=0)
tk.Label(text="Miles").grid(row=0,column=2)
km = tk.Label(text="0")
km.grid(row=1,column=1)
tk.Label(text="Km").grid(row=1,column=2)
ip = tk.Entry(width=7)
ip.grid(row=0,column=1)
tk.Button(text="Calculate",command=convert).grid(row=2,column=1)

tk.mainloop()