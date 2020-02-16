from scipy.constants import c

def classificarUnidade(tipo):

    unidade = ""
    valor = 1

    if tipo == "Ondas de Rádio":
        unidade = "m"
        valor = 1
    elif tipo == "Micro-Ondas":
        unidade = "mm"
        valor = 10 ** 3
    elif tipo in range("Infravermeho", "Raios X", "Raios Gama", "Ultravioleta", "Visível"):
        unidade = "nm"
        valor = 10 ** 9

    return unidade, valor

def classificarOnda(comp):
    tipo = ""

    if (comp >= 1.0 and comp <= 1.*10**6):
        tipo = "Ondas de Rádio"
    elif (comp >= 1.0*10**-4 and comp <= 1.0):
        tipo = "Micro-Ondas"
    elif (comp >= 700.0*10**-9 and comp <= 1.0*10**-4):
        tipo = "Infravermeho"
    elif (comp >= 400.0*10**-9 and comp <= 700.0*10**-9):
        tipo = "Visível"
    elif (comp >= 1.0*10**-8 and comp <= 400.0*10**-9):
        tipo = "Ultravioleta"
    elif (comp >= 1.0*10**-12 and comp <= 1.0*10**-8):
        tipo = "Raios X"
    elif (comp >= 1.0*10**-14 and comp <= 1.0*10**-12):
        tipo = "Raios Gama"

    unidade, valor = classificarUnidade(tipo)

    return tipo, unidade, valor

def CalculaFrequencia(freq):

    comp = c/freq
    #print(c, freq)
    tipo, unidade, valor = classificarOnda(comp)

    comp *= valor

    print("--> Comprimento de Onda: " + str(comp) + " " + unidade)
    print("--> Tipo de Onda: " + tipo + "\n")

    return

def pedeFrequencia():

    freq = input("\nDigite a frequência (Ex. 700 Hz): ")

    valor = float(freq[0:-3])

    CalculaFrequencia(valor)