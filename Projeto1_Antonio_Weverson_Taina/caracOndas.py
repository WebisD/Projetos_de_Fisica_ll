from scipy.constants import c, pi
import numpy as np

def numeroDaOnda(opcao, entrada, und):
    if opcao == 1:                  # entrada = frequencia
        nOnda = (2*pi*entrada)/c
    elif opcao == 2:                # entrada = comprimento de onda
        expo = analisaUnidade(und)
        entrada *= expo
        nOnda = (2*pi)/entrada

    return "--> Numero da Onda: "+ np.format_float_scientific(np.float32(nOnda), precision=3) + " rad/m"


def freqAngular(opcao, entrada, und):
    if opcao == 1:                # entrada = frequencia
        w = 2*pi*entrada
    elif opcao == 2:              # entrada = comprimento de onda
        expo = analisaUnidade(und)
        entrada *= expo
        w = (2*pi*c)/entrada

    return "--> Frequência Angular: " + np.format_float_scientific(np.float32(w), precision=3) + " rad/s"


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