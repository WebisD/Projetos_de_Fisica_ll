from tkinter import *
from tkinter.ttk import Combobox
import equacoesPolarizador

def open1():
    window = Tk()
    window.title ("1 Polarizador")
    window.geometry('300x200')

    label = Label(window, text = "Qual a intensidade de luz?")
    label.place(x = 50, y = 20)
    entrada = Entry(window, width = 18, font=('Arial', 12))
    entrada.place(x=50, y = 40)
    result = Label(window)
    result.place(x = 50, y = 150)

    def calcula():
        i1Value = float(entrada.get())
        result['text'] = "O resultado é: I0: " + str(i1Value) + " e  I = " + str(equacoesPolarizador.halfLaw(i1Value))

    btn = Button(window, text = "Calcular", command=calcula)
    btn.place(x = 50, y = 80)

    window.mainloop()

def open2():
    window = Tk()
    window.title ("2 Polarizadores")
    window.geometry('350x300')

    label = Label(window, text = "Qual a intensidade de luz?")
    label.place(x = 50, y = 20)
    entrada = Entry(window, width = 18, font=('Arial', 12))
    entrada.place(x=50, y =50)
    label = Label(window, text = "Qual I possui essa intensidade?")
    label.place(x = 50, y = 80)
    combobox = Combobox(window)
    combobox['values'] = (0,1,2)
    combobox.current(1)
    combobox.place(x = 50, y = 110)
    label = Label(window, text = "Qual os ângulos?")
    label.place(x = 50, y = 140)
    anguloI0 = Entry(window, width = 5, font=('Arial', 12))
    anguloI0.place(x=50, y =170)
    anguloI1 = Entry(window, width = 5, font=('Arial', 12))
    anguloI1.place(x=120, y =170)

    result = Label(window)
    result.place(x = 50, y = 250)

    def calcula():
        intensidadeValue = entrada.get()
        polarizador = int(combobox.get())
        I0 = 0
        I1 = 0
        I2 = 0

        if polarizador == 0:
            I0 = intensidadeValue
            I1 = equacoesPolarizador.halfLaw(I0)
            #I2 = equacoesPolarizador.malusLaw(I1,float(anguloI0.get()))
        elif polarizador == 1:
            I0 = equacoesPolarizador.reverseHalfLaw(I1)
            I1 = intensidadeValue
            #I2 = equacoesPolarizador.malusLaw(I1,)
        else:
            I0 = equacoesPolarizador.reverseHalfLaw(I1)
            #I1 = equacoesPolarizador.reverseMalusLaw(I2)
            I2 = intensidadeValue
            
            
        result['text'] = "O resultado é: I0" + str(I0) + " e I1 = " + str(I1) + " e I2 = " + str(I2)


    btn = Button(window, text = "Calcular", command=calcula)
    btn.place(x = 50, y = 200)

    window.mainloop()

def open3():
    window = Tk()
    window.title ("3 Polarizadores")
    window.geometry('350x300')

    label = Label(window, text = "Qual a intensidade de luz?")
    label.place(x = 50, y = 20)
    entrada = Entry(window, width = 18, font=('Arial', 12))
    entrada.place(x=50, y =50)
    label = Label(window, text = "Qual polarizador possui essa intensidade?")
    label.place(x = 50, y = 80)
    combobox = Combobox(window)
    combobox['values'] = (1,2,3)
    combobox.current(1)
    combobox.place(x = 50, y = 110)
    label = Label(window, text = "Qual os ângulos?")
    label.place(x = 50, y = 140)
    anguloI0 = Entry(window, width = 5, font=('Arial', 12))
    anguloI0.place(x=50, y =170)
    anguloI1 = Entry(window, width = 5, font=('Arial', 12))
    anguloI1.place(x=120, y =170)
    anguloI2 = Entry(window, width = 5, font=('Arial', 12))
    anguloI2.place(x=190, y =170)

    result = Label(window)
    result.place(x = 50, y = 250)

    def calcula():
        intensidadeValue = entrada.get()
        polarizador = int(combobox.get())
        result['text'] = "O resultado é: " + str(1)

    btn = Button(window, text = "Calcular", command=calcula)
    btn.place(x = 50, y = 200)

    window.mainloop()