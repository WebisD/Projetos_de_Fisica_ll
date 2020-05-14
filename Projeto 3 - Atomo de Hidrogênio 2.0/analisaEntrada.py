import energiaCinetica as eC
import energiaPotencial as eP
import energiaTotal as eT
import raioOrbita as rO
import ComprimentoOndaTransição as cPT
import ComprimentoOndaTransicaoSerie as cPTS

def getInputEnergy(n):
    print(n)
    try:
        value = float(n.replace(',','.'))
    except ValueError:
        return ["Error", "Não foi possível interpretar o valor digitado como um número"]

    print(value)
    number = round(value)

    if (abs(value - number) <= 0.10000000000000009):
        E_Cinetica = eC.calcEnergiaCinetica(number)
        E_Potencial = eP.calcEnergiaPotencial(number)
        E_Total = eT.calcEnergiaTotal(number)
        R_Orbita = rO.calcRaio(number)
        Resposta = '''Energia Cinética: {} eV
        
Energia Potencial: {} eV

Energia Total: {} eV

Raio da Órbita: {} nm
        '''
        return ["Success", Resposta.format(E_Cinetica, E_Potencial, E_Total, R_Orbita)]
    else:
        return ["Error", "Digite um valor inteiro"]


def tryFloat(n):
    try:
        value = float(n.replace(',','.'))
        return True
    except ValueError:
        return False

def tryInt(value, number):
    if (abs(value - number) <= 0.10000000000000009):
        return True
    else:
        return False

def getInputComp(ni, nf):

    if not tryFloat(ni):
        return ["Error", "Não foi possível interpretar o valor em NI como um número"]
    if not tryFloat(nf):
        return ["Error", "Não foi possível interpretar o valor em NF como um número"]

    valueNi = float(ni.replace(',', '.'))
    valueNf = float(nf.replace(',', '.'))

    numberNi = round(valueNi)
    numberNf = round(valueNf)

    if not tryInt(valueNi, numberNi):
        return ["Error", "Digite um valor inteiro em NI"]
    if not tryInt(valueNf, numberNf):
        return ["Error", "Digite um valor inteiro em NF"]

    comp = cPT.calcularComprimentoTransacao(numberNi, numberNf)
    Resposta = "Comprimento de Onda emitido pelo átomo:\n\n                      λ = {0:.4e} m"

    return ["Success", Resposta.format(comp)]

def getInputSerie(ni, serie):
    if not tryFloat(ni):
        return ["Error", "Não foi possível interpretar o valor em NI como um número"]

    valueNi = float(ni.replace(',', '.'))
    numberNi = round(valueNi)

    if not tryInt(valueNi, numberNi):
        return ["Error", "Digite um valor inteiro em NI"]

    result = cPTS.calcComprimentoComSerie(numberNi, serie)
    print(result)
    if result[0] != "Error":
        print("entrou")
        Resposta = '''Comprimento de Onda emitido pelo átomo:\n\n                      λ = {0:.4e} m\n\n
        Cor do fóton emitido: {1}'''
        return ["Success", Resposta.format(result[0], result[1])]
    else:
        return result