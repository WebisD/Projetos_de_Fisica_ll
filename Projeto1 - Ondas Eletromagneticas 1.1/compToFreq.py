from scipy.constants import c
import numpy as np

def classificarOnda(comp):
    tipo = ""

    if (comp >= 1.0 * 10 ** -(0.5)):
        tipo = "Ondas de Rádio"
    elif (comp < 1.0 * 10 ** -(0.5) and comp >= 1.0 * 10 ** -3):
        tipo = "Micro-Ondas"
    elif (comp < 1.0 * 10 ** -3 and comp >= 400 * 10 ** -9):
        tipo = "Infravermeho"
    elif (comp < 400.0 * 10 ** -9 and comp >= 700.0 * 10 ** -9):
        tipo = "Visível"
    elif (comp < 700 * 10 ** -9 and comp >= 400.0 * 10 ** -7.5):
        tipo = "Ultravioleta"
    elif (comp < 1.0 * 10 ** -7.5 and comp >= 1.0 * 10 ** -10.5):
        tipo = "Raios X"
    elif (comp < 1.0 * 10 ** -10.5 and comp >= 1.0 * 10 ** -12):
        tipo = "Raios Gama"

    return tipo

def analisaUnidade(unidade):
    valor = 1
    if unidade == "nm":
        valor = 10**-9
    elif unidade == "mm":
        valor = 10**-6
    elif unidade == "m":
        valor = 1
    elif unidade == "km":
        valor = 10**3
    else:
        print("ta errado")
        pedeComprimento()
    return valor

def calculaFrequencia(comp):
    f = c/comp
    tipo = classificarOnda(comp)

    #print("Frequência: " + "{:e}".format(f) + " Hz")
    print("--> Frequência: " + np.format_float_scientific(np.float32(f), precision=3) + " Hz")
    print("--> Tipo de Onda: " + tipo + "\n")

    return

def pedeComprimento():

    comp = input("\nDigite o comprimento de onda (Ex. 700 km): ")

    num, unidade = comp.split(" ")
    num = float(num)

    expoente = analisaUnidade(unidade)

    valor = num*expoente

    calculaFrequencia(valor)

    return

