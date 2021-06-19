from scipy.constants import c
import ClassOndaCarac as freq
import numpy as np

def analisaUnidade(unidade):
    valor = 1
    if unidade == "nm":
        valor = 10 ** -9
    elif unidade == "um":
        valor = 10 ** -6
    elif unidade == "mm":
        valor = 10 ** -3
    elif unidade == "cm":
        valor = 10 ** -2
    elif unidade == "m":
        valor = 1
    elif unidade == "km":
        valor = 10 ** 3
    return valor

def calculaFrequencia(comp):
    f = c/comp

    tipo = freq.classificarOnda(comp)

    return "--> Frequência: " + str(np.format_float_scientific(np.float32(f), precision=3)) + " Hz" + "\n--> Tipo de Onda: " + tipo

