from tkinter import *
from tkinter.ttk import Combobox
import equacoesPolarizador

def open1():
    window = Tk()
    window.title ("1 Polarizador")
    window.geometry('350x300')

    label = Label(window, text = "Qual a intensidade da luz em W/m² ?")
    label.place(x = 50, y = 20)
    entrada = Entry(window, width = 18, font=('Arial', 12))
    entrada.place(x=50, y = 40)

    label = Label(window, text="Qual I possui essa intensidade?")
    label.place(x=50, y=80)
    combobox = Combobox(window)
    combobox['values'] = (0, 1)
    combobox.current(0)
    combobox.place(x=50, y=110)

    result = Label(window)
    result.place(x = 50, y = 190)

    def calcula():
        intensidade = int(combobox.get())

        if intensidade == 0:
            I0 = float(entrada.get())
            I1 = equacoesPolarizador.halfLaw(I0)
        elif intensidade == 1:
            I1 = float(entrada.get())
            I0 = equacoesPolarizador.reverseHalfLaw(I1)
        result['text'] = " I0 = " + str(I0) + " W/m²\nI1 = " + str(I1)+ " W/m²"

    btn = Button(window, text = "Calcular", command=calcula)
    btn.place(x = 50, y = 150)

    window.mainloop()

def open2():
    window = Tk()
    window.title ("2 Polarizadores")
    window.geometry('350x300')

    label = Label(window, text = "Qual a intensidade de luz em W/m² ?")
    label.place(x = 50, y = 20)
    entrada = Entry(window, width = 18, font=('Arial', 12))
    entrada.place(x=50, y =50)
    label = Label(window, text = "Qual I possui essa intensidade?")
    label.place(x = 50, y = 80)
    combobox = Combobox(window)
    combobox['values'] = (0,1,2)
    combobox.current(1)
    combobox.place(x = 50, y = 110)
    label = Label(window, text = "Qual o ângulo θ1 ?")
    label.place(x = 50, y = 140)
    angulo = Entry(window, width = 5, font=('Arial', 12))
    angulo.place(x=50, y =160)

    result = Label(window)
    result.place(x = 50, y = 250)

    def calcula():
        intensidadeValue = float(entrada.get())
        polarizador = int(combobox.get())
        I0 = 0
        I1 = 0
        I2 = 0
        anguloI1 = float(angulo.get())
        if polarizador == 0:
            I0 = intensidadeValue
            I1 = equacoesPolarizador.halfLaw(I0)
            I2 = equacoesPolarizador.malusLaw(I1,anguloI1)
        elif polarizador == 1:
            I1 = intensidadeValue
            I0 = equacoesPolarizador.reverseHalfLaw(I1)
            I2 = equacoesPolarizador.malusLaw(I1, anguloI1)
        else:
            I2 = intensidadeValue
            I1 = equacoesPolarizador.reverseMalusLaw(I2, anguloI1)
            I0 = equacoesPolarizador.reverseHalfLaw(I1)

        result['text'] = "I0 = " + str(I0) + " W/m²\nI1 = " + str(I1) + " W/m²\nI2 = " + str(I2) + " W/m²"

    btn = Button(window, text = "Calcular", command=calcula)
    btn.place(x = 50, y = 210)

    window.mainloop()

def open3():
    window = Tk()
    window.title ("3 Polarizadores")
    window.geometry('350x300')

    label = Label(window, text = "Qual a intensidade de luz em W/m² ?")
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
