from scipy.constants import c
import numpy as np
#c = 3*10**8

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
    f = c/comp;

    #print("Frequência: " + "{:e}".format(f) + " Hz")
    print("--> Frequência: " + np.format_float_scientific(np.float32(f), precision=3) + " Hz")

    return

def pedeComprimento():

    comp = input("\nDigite o comprimento de onda (Ex. 700 nm): ")

    num, unidade = comp.split(" ")
    num = float(num)

    expoente = analisaUnidade(unidade)

    valor = num*expoente

    calculaFrequencia(valor)

    return

