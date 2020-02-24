from scipy.constants import c
import numpy as np
#c = 3*10**8

def analisaUnidade(unidade):
    valor = 1

    if unidade == "nT":
        valor = 10**-9
    elif unidade == "mT":
        valor = 10**-3
    elif unidade == "kT":
        valor = 10**3
    elif unidade == "T":
        valor = 1
    elif unidade == "MT":
        valor = 10**6
    elif unidade == "GT":
        valor = 10**9
    else:
        print("ta errado")
        pedeBm()
    return valor

def calculaEm(valueBm):
    em = valueBm*c

    print("--> Valor do campo elétrico: " + np.format_float_scientific(np.float32(em), precision=3) + " V/m")

def pedeEm():

    Em = input("\nDigite o valor do campo magnético máximo (Ex. 700 GT): ")

    num, unidade = comp.split(" ")
    num = float(num)

    expoente = analisaUnidade(unidade)
    valor = num*expoente
    calculaEm(valor)

