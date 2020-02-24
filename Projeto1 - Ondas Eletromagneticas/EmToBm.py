from scipy.constants import c
import numpy as np
#c = 3*10**8

def analisaUnidade(unidade):
    valor = 1

    if unidade == "mV/m":
        valor = 10**-3
    elif unidade == "kV/m":
        valor = 10**3
    elif unidade == "MV/m":
        valor = 10**6
    elif unidade == "V/m":
        valor = 1
    else:
        print("ta errado")
        pedeEm()
    return valor

def calculaBm(valueEm):
    bm = valueEm/c

    print("--> Valor do campo magnético: " + np.format_float_scientific(np.float32(bm), precision=3) + " T")

def pedeEm():

    Em = input("\nDigite o valor do campo elétrico máximo (Ex. 700 kV/m): ")

    num, unidade = comp.split(" ")
    num = float(num)

    expoente = analisaUnidade(unidade)
    valor = num*expoente
    calculaBm(valor)

