from scipy.constants import c, pi

def classificarOnda(comp):
    tipo = ""

    if (comp < 1.0 * 10 ** -10.5 and comp >= 1.0 * 10 ** -12):
        tipo = "Raios Gama"
    elif (comp < 1.0 * 10 ** -7.5 and comp >= 1.0 * 10 ** -10.5):
        tipo = "Raios X"
    elif (comp < 400 * 10 ** -9 and comp >= 1.0 * 10 ** -7.5):
        tipo = "Ultravioleta"
    elif (comp < 700.0 * 10 ** -9 and comp >= 400.0 * 10 ** -9):
        tipo = "Visível"
    elif (comp < 1.0 * 10 ** -3 and comp >= 700 * 10 ** -9):
        tipo = "Infravermeho"
    elif (comp < 1.0 * 10 ** -(0.5) and comp >= 1.0 * 10 ** -3):
        tipo = "Micro-Ondas"
    elif (comp >= 1.0 * 10 ** -(0.5)):
        tipo = "Ondas de Rádio"

    return tipo

def freqAngToComp(freqAngularValue):
    comp = (2*pi*c)/freqAngularValue
    return "--> Tipo de Onda: " + classificarOnda(comp)

def numeroOndaToComp(numOndaValue):
    comp = (2*pi)/numOndaValue
    return "--> Tipo de Onda: " + classificarOnda(comp)