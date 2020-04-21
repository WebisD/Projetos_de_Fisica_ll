import number
import energiaTotal
import math

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
    return valor

def calcFoton(comprimento, unidade):
    #fazer a validação dos comprimentos absorvidos pelo hidrogenio
    energia = (number.h * number.c)/(comprimento*unidade)
    return energia

def nFinal(energiaFoton):
    estadoFundamental = energiaTotal.calcEnergiaTotal(1)
    energiaFinal = estadoFundamental + energiaFoton

    valorN = math.sqrt(-13.6/energiaFinal)

    return valorN
    

