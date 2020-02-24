from scipy.constants import c
from scipy.constants import pi

import numpy as np
#c = 3*10**8

def analisaUnidade(unidade):
    valor = 1

    if unidade == "mHz":
        valor = 10**-3
    elif unidade == "kHz":
        valor = 10**3
    elif unidade == "MHz":
        valor = 10**6
    elif unidade == "Hz":
        valor = 1
    else:
        print("ta errado")
        pedeEm()
    return valor

def calculaFreqAngAndK(freq):
    k = 2*pi/c*freq
    freqAng = 2*pi*freq

    print("--> Número de onda: " + np.format_float_scientific(np.float32(k), precision=3) + " m")
    print("--> Frequência Angular: " + np.format_float_scientific(np.float32(freqAng), precision=3) + " Hz")

def pedeComprimento():

    freq = input("\nDigite a frequência (Ex. 700 Hz): ")

    num, unidade = freq.split(" ")
    num = float(num)

    expoente = analisaUnidade(unidade)
    valor = num*expoente
    calculaFreqAngAndK(valor)


