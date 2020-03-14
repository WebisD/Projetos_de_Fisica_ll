import compToFreq as freq
import freqToComp as comp
import caracOndas as ondas
import ClassOndaCarac as classOnda
import campos as campos
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import ImageTk, Image

def ondaW():
    w = Tk()
    w.title("Tipo de onda com ω")
    w.geometry('400x400')

    def chamaFunc():
        entry = entrada.get()
        res['text'] = classOnda.freqAngToComp(float(entry))

    label = Label(w, text="Digite o valor de ω em rad/s:", font='Arial 12')
    label.place(relx=0.3, rely=0.2)
    res = Label(w, font='Arial 12')
    res.place(relx=0.05, rely=0.8)

    entrada = Entry(w, width=14, font='Arial 12')
    entrada.place(relx=0.35, rely=0.4)

    bt = Button(w, text="Converter", font='Arial 12', command=chamaFunc)
    bt.place(relx=0.42, rely=0.6)

    w.mainloop()

def ondaK(): #tipo da onda com num da onda
    w = Tk()
    w.title("Tipo de onda com k")
    w.geometry('400x400')

    def chamaFunc():
        entry = entrada.get()
        res['text'] = classOnda.numeroOndaToComp(float(entry))

    label = Label(w, text="Digite o valor de k em rad/m:", font='Arial 12')
    label.place(relx=0.3, rely=0.2)
    res = Label(w, font='Arial 12')
    res.place(relx=0.05, rely=0.8)

    entrada = Entry(w, width=14, font='Arial 12')
    entrada.place(relx=0.35, rely=0.4)

    bt = Button(w, text="Converter", font='Arial 12', command=chamaFunc)
    bt.place(relx=0.42, rely=0.6)

    w.mainloop()

def opChamaNumeFreq(func):
    w = Tk()
    w.title("Cálculo com f ou λ")
    w.geometry('400x400')

    #o func serve para saber se o pedido veio do Num de Onda ou da Freq Angular

    def pedeFreq():
        label1['text'] = "Digite a frequência em Hz:"
        resul['text'] = ''

        def manda():
            entry = entrada.get()
            if entry != '':
                if func == "num":  # freq num de onda com freq
                    resul['text'] = str(ondas.numeroDaOnda(1, float(entry), 0))
                elif func == "freq":  # quer freq angular com freq
                    resul['text'] = str(ondas.freqAngular(1, float(entry), 0))

        entrada = Entry(w)
        entrada.place(relx=0.3, rely=0.5)

        cbx = Combobox(w, state='readonly', font='Arial 10', width=5)
        cbx['values'] = ('Hz')
        cbx.set('Hz')
        cbx.place(relx=0.7, rely=0.5)

        btn1 = Button(w, text="Calcular", font='Arial 10', command=manda)
        btn1.place(relx=0.38, rely=0.6)

    def pedeComp():
        resul['text'] = ''
        label1['text'] = "Digite o λ e selecione a unidade:"

        def manda():
            entry = entrada.get()
            cmbx = cbx.get()

            if entry != '':
                if func == "num":  # quer num de onda com comp
                    resul['text'] = str(ondas.numeroDaOnda(2, float(entry), cmbx))
                elif func == "freq":  # quer freq com comp
                    resul['text'] = str(ondas.freqAngular(2, float(entry), cmbx))

        entrada = Entry(w)
        entrada.place(relx=0.3, rely=0.5)
        cbx = Combobox(w, state='readonly', font='Arial 10', width=5)
        cbx['values'] = ('nm', 'um', 'mm', 'cm', 'm', 'km')
        cbx.set('m')
        cbx.place(relx=0.7, rely=0.5)

        btn1 = Button(w, text="Calcular", font='Arial 10', command=manda)
        btn1.place(relx=0.38, rely=0.6)

    label = Label(w, text="Selecione o dado que deseja usar:", font='Arial 12')
    label.place(relx=0.2, rely=0.1)

    frequencia = Button(w, text="Frequência", command=pedeFreq)
    frequencia.place(relx=0.2, rely=0.2)
    compri = Button(w, text="Comprimento de onda", command=pedeComp)
    compri.place(relx=0.5, rely=0.2)

    label1 = Label(w, text="", font='Arial 12')
    label1.place(relx=0.2, rely=0.4)

    resul = Label(w, text="", font='Arial 12')
    resul.place(relx=0.1, rely=0.8)

    w.mainloop()

def calcEm():
    w = Tk()
    w.title("Cálculo do campo Em")
    w.geometry('400x400')

    def chamaEm():
        bm = entrada.get()
        em['text'] = campos.MagneticoToEletrico(float(bm))

    freqL = Label(w, text="Digite o valor de Bm em T:", font='Arial 12')
    freqL.place(relx=0.3, rely=0.2)
    em = Label(w, font='Arial 12')
    em.place(relx=0.05, rely=0.8)

    entrada = Entry(w, width=14, font='Arial 12')
    entrada.place(relx=0.35, rely=0.4)

    bt = Button(w, text="Converter", font='Arial 12', command=chamaEm)
    bt.place(relx=0.42, rely=0.6)

    w.mainloop()

def calcBm():
    w = Tk()
    w.title("Cálculo do campo Bm")
    w.geometry('400x400')

    def chamaBm():
        em = entrada.get()
        bm['text'] = campos.EletricoToMagnetico(float(em))

    freqL = Label(w, text="Digite o valor de Em em V/m:", font='Arial 12')
    freqL.place(relx=0.3, rely=0.2)
    bm = Label(w, font='Arial 12')
    bm.place(relx=0.05, rely=0.8)

    entrada = Entry(w, width=14, font='Arial 12')
    entrada.place(relx=0.35, rely=0.4)

    bt = Button(w, text="Converter", font='Arial 12', command=chamaBm)
    bt.place(relx=0.42, rely=0.6)

    w.mainloop()

def toComp():
    w = Tk()
    w.title("Conversão f para λ")
    w.geometry('400x400')

    def chamaComp():
        freq = entrada.get()
        if freq == '0':
            res = messagebox.showinfo('Aviso', 'Não existe onda com frequência igual a 0.')
        else:
            compL['text'] = comp.CalculaComp(float(freq))

    freqL = Label(w, text="Digite a frequência em Hz:", font='Arial 12')
    freqL.place(relx=0.3, rely=0.2)
    compL = Label(w, font='Arial 12')
    compL.place(relx=0.05, rely=0.8)

    entrada = Entry(w, width=14, font='Arial 12')
    entrada.place(relx=0.35, rely=0.4)

    bt = Button(w, text="Converter", font='Arial 12', command=chamaComp)
    bt.place(relx=0.42, rely=0.6)

    w.mainloop()

def toFreq():
    w = Tk()
    w.title("Conversão λ para f")
    w.geometry('400x400')

    def chamaFreq():
        und = cbx.get()
        num = entrada.get()
        if num == '0':
            res = messagebox.showinfo('Aviso', 'Não existe onda com λ igual a 0.')
        elif und != "" and num != "":
            exp = freq.analisaUnidade(und)
            resultado['text'] = freq.calculaFrequencia(float(num) * exp)

    comp = Label(w, text="Digite o λ e selecione a unidade:", font='Arial 12')
    comp.place(relx=0.2, rely=0.2)
    resultado = Label(w, font='Arial 12')
    resultado.place(relx=0.2, rely=0.8)

    entrada = Entry(w, width=14, font='Arial 12')
    entrada.place(relx=0.2, rely=0.4)

    cbx = Combobox(w, state='readonly', font='Arial 10', width=10)
    cbx['values'] = ('nm', 'um', 'mm', 'cm', 'm', 'km')
    cbx.set('m')
    cbx.place(relx=0.6, rely=0.4)

    bt = Button(w, text="Converter", font='Arial 12', command=chamaFreq)
    bt.place(relx=0.4, rely=0.6)

    w.mainloop()

def main():
    janela = Tk()

    janela.title("Física")
    janela.geometry('1100x650')
    janela.configure(background='darkblue')

    img = ImageTk.PhotoImage(Image.open("fundo.jpg"))
    l = Label(image=img)
    l.pack()

    def chamaFuncao():
        txtO = cbxO.get()   #ondas
        txtC = cbxE.get()  # campos

        if txtO == "Conversão de λ para f":
            cbxO.set('')
            toFreq()
        elif txtO == "Conversão de f para λ":
            cbxO.set('')
            toComp()
        elif txtC == "Cálculo do campo Bm":
            cbxE.set('')
            calcBm()
        elif txtC == "Cálculo do campo Em":
            cbxE.set('')
            calcEm()
        elif txtC == "Número de onda":
            cbxE.set('')
            opChamaNumeFreq("num")
        elif txtC == "Frequência angular":
            cbxE.set('')
            opChamaNumeFreq("freq")
        elif txtC == "Tipo de onda com k":
            cbxE.set('')
            ondaK()
        elif txtC == "Tipo de onda com ω":
            cbxE.set('')
            ondaW()

    ondasElet = Label(janela, text="Ondas Eletromagnéticas", font='Arial 15')
    ondasElet.place(relx=0.6, rely=0.2, anchor=W)
    cbxO = Combobox(janela, state='readonly', width=25, font='Arial 12')
    cbxO['values'] = ("Conversão de λ para f", "Conversão de f para λ")
    cbxO.place(relx=0.6, rely=0.3, anchor=W)
    bt = Button(janela, text="Enviar", font='Arial 12', command=chamaFuncao)
    bt.place(relx=0.675, rely=0.4, anchor=W)

    cEletEMag = Label(janela, text="Campos Elétrico e Magnético", font='Arial 15')
    cEletEMag.place(relx=0.6, rely=0.6, anchor=W)
    cbxE = Combobox(janela, state='readonly', width=25, font='Arial 12')
    cbxE['values'] = ("Cálculo do campo Bm", "Cálculo do campo Em", "Número de onda", "Frequência angular", "Tipo de onda com k",
                      "Tipo de onda com ω")
    cbxE.place(relx=0.6, rely=0.7, anchor=W)
    bt2 = Button(janela, text="Enviar", font='Arial 12', command=chamaFuncao)
    bt2.place(relx=0.675, rely=0.8, anchor=W)

    janela.mainloop()

main()

