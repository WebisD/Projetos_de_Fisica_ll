from tkinter import *
from tkinter.ttk import Combobox
import polarizadores

def inicializa():
    window = Tk()
    window.title ("Polarização - 1")
    window.geometry('300x200')

    #cria a combobox
    combobox = Combobox(window, state="readonly")
    combobox['values'] = (1, 2, 3)
    combobox.current(0)
    combobox.place(x=50, y=50)

    def show():
        numeroPolarizadores = int(combobox.get())
        if numeroPolarizadores == 1:
            polarizadores.open1()
        elif numeroPolarizadores == 2:
            polarizadores.open2()
        else:
            polarizadores.open3()

    btn = Button(window, text = "Avançar", command=show)
    btn.place(relx = 0.5, rely =0.5, anchor=CENTER)

    label = Label(window, text = "Quantos polarizadores deseja?")
    label.place(x = 50, y = 20)

    window.mainloop()