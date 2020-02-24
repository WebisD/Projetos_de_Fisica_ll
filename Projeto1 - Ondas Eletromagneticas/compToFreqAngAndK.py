from scipy.constants import c
from scipy.constants import pi

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
        calculaFreqAngAndK()
    return valor

def calculaFreqAngAndK(comp):
    k = 2*pi/comp
    freqAng = (2*pi)*(comp/c)

    print("--> Número de onda: " + np.format_float_scientific(np.float32(k), precision=3) + " m")
    print("--> Frequência Angular: " + np.format_float_scientific(np.float32(freqAng), precision=3) + " Hz")

def pedeComprimento():

    comp = input("\nDigite o comprimento de onda (Ex. 700 nm): ")

    num, unidade = comp.split(" ")
    num = float(num)

    expoente = analisaUnidade(unidade)
    valor = num*expoente
    calculaFrequencia(valor)


