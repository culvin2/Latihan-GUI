import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("PYTHON GUI")
aLabel = ttk.Label(win,text="100 JUTA GRATIS? CLICK !!")
aLabel.grid(column = 0, row = 0)

def clickMe():
    action.configure(text = "SELAMAT ANDA MENDAPAT UANG 100 JT")
    aLabel.configure(foreground ="red")
action = ttk.Button(win,text="CLICK ME !!",command = clickMe)
action.grid(column = 1,row = 0)

bLabel = ttk.Label(win,text="Obat Pembesar T***T")
bLabel.grid(column=0,row=1)

def clickMe():
    action.configure(text="Klik Untuk Mendapatkan Rasa Yang Tidak Pernah Di Rasakan")
    bLabel.configure(foreground="green")
action = ttk.Button(win,text="Ketuk Disini !!",command = clickMe)
action.grid(column = 1, row = 1  )

win.mainloop()