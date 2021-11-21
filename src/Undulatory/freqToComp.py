from scipy.constants import c
import ClassOndaCarac as freq
import numpy as np

def classificarUnidade(comp):
    tipo = freq.classificarOnda(comp)
    unidade = ""
    valor = 1

    if tipo == "Ondas de Rádio":
        unidade = "m"
        valor = 1
    elif tipo == "Micro-Ondas":
        unidade = "mm"
        valor = 10 ** 3
    elif tipo in ("Infravermeho", "Raios X", "Raios Gama", "Ultravioleta", "Visível"):
        unidade = "nm"
        valor = 10 ** 9

    return tipo, unidade, valor

def CalculaComp(freq):

    comp = c/freq

    tipo, unidade, valor = classificarUnidade(comp)

    comp *= valor

    return "--> Comprimento de Onda: " + np.format_float_scientific(np.float32(comp), precision=3) + " "\
           + unidade + "\n--> Tipo de Onda: " + tipo