import constantes
import energiaTotal
import math
import analisaEntrada as analiseNivel

def analisaUnidade(unidade):
    valor = 1

    if unidade == "nm":
        valor = 10 ** -9
    elif unidade == "μm":
        valor = 10 ** -6
    elif unidade == "m":
        valor = 1
    elif unidade == "km":
        valor = 10 ** 3
    return valor

def calcFoton(comprimento, unidade):
    # fazer a validação dos comprimentos absorvidos pelo hidrogenio
    energia = (constantes.h_eVs * constantes.c) / (comprimento * unidade)
    return energia

def nFinal(comp, unidade):
    und = analisaUnidade(unidade)
    print(comp * und)
    energiaFoton = calcFoton(comp, und)
    print(energiaFoton)

    if energiaFoton > 10.2:
        estadoFundamental = energiaTotal.calcEnergiaTotal(1)
        difEnergia = energiaFoton + estadoFundamental
        print(difEnergia)
        nivel = math.sqrt(abs(-13.6 / difEnergia))

        if analiseNivel.tryInt(round(nivel), nivel):
            return "Resultado", int(nivel)
        else:
            return "Erro", "O átomo de hidrogênio não absorve um fóton com esse comprimento de onda."
    else:
        if energiaFoton < 10.2:
            return "Erro", "Digite um comprimento de onda maior, esse fóton irá ionizar o átomo de hidrogênio."
