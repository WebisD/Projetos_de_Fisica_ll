import math

def grausToRadians(valorGraus):
    radiano = math.radians(valorGraus)
    return radiano

def cosseno(Graus):
    Radiano = grausToRadians(Graus)
    valorCosseno = math.cos(Radiano)

    #retorna o cos^2
    return valorCosseno**2

