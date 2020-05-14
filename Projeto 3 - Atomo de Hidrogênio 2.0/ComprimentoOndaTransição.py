import energiaTotal
import constantes

def calcularComprimentoTransacao(nInitial, nFinal):
    energiaInicial = energiaTotal.calcEnergiaTotal(nInitial)
    energiaFinal = energiaTotal.calcEnergiaTotal(nFinal)

    variacaoEnergia = energiaInicial - energiaFinal
    comprimento = (constantes.h_eVs * constantes.c) / variacaoEnergia

    return comprimento