import energiaTotal
import number

def calcularComprimentoTransacao(nInitial, nFinal):
    energiaInicial = energiaTotal.calcEnergiaTotal(nInitial)
    energiaFinal = energiaTotal.calcEnergiaTotal(nFinal)

    variacaoEnergia = energiaInicial - energiaFinal
    comprimento = (number.h * number.c)/variacaoEnergia

    return comprimento