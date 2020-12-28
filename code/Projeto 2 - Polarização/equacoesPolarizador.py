import cos

def halfLaw(I0):
    I = I0/2

    return I

def reverseHalfLaw(I):
    I0 = I*2

    return I0

def malusLaw(I0, angulo):
    I = I0*(cos.cosseno(angulo))

    return I

def reverseMalusLaw(I2, angulo):
    I1 = I2/(cos.cosseno(angulo))

    return I1
